#!/usr/bin/env python
from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
from .models import Log
from .models import Command
from .serializers import LogSerilizer
from .serializers import CommandSerilizer

import rospy
from std_msgs.msg import String
import pickledb
import os
from os.path import expanduser
import datetime

# Create your views here.

dir = expanduser("~") + '/Desktop/'
def create_directories():
    global dir
    if not os.path.exists(dir + 'cabinet_db'):
        os.makedirs(dir + 'cabinet_db')
    dir = dir + 'cabinet_db/'


def create_uid_directories(num):
    time = datetime.datetime.today().strftime('%Y-%m-%d_%H:%M:%S')

    if not os.path.exists(dir + '%s'%num ):
        os.makedirs(dir + '%s'%num )

    if not os.path.exists(dir + '%s'%num + '/' + time):
        os.makedirs(dir + '%s'%num + '/' + time)
    print (dir + '%s'%num + '/' + time)
    return str(dir + '%s'%num + '/' + time)


def search_name(name,f_name,_db):
    number = 0
    while True:
        info = _db.get('%d'%number)
        print (info)
        if info == None:
            print('False')
            return False,number
        else :
            if info[0] == name and info[1] == f_name:
                print('true')
                return True,number
        number += 1




db = pickledb.load('uid.db',False)
db.dump()

parrot_command = rospy.Publisher('web/parrot_commands', String, queue_size=10)
patient_uid = rospy.Publisher('web/patient_uid', String, queue_size=10)
patient_uid_directories = rospy.Publisher('web/patient_uid/dir', String, queue_size=10)
rospy.init_node('web_logger', anonymous=False)
create_directories()

class LogView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerilizer

    def perform_create(self, serializer):
        global db
        serializer.save()

        info = [serializer.data['name'],serializer.data['familyName'],serializer.data['phoneNumber']]
        res,num = search_name(info[0],info[1],db)
        if res == False:
            db.set('%d'%num,info)
            db.dump()



        patient_uid_directories.publish('%s'%create_uid_directories(num))

        if not serializer.data['name'] == '-1':
            patient_uid.publish('%d'%num)
        else :
            patient_uid.publish('-1')

        #You can acces name & familyName & id & phoneNumber
        # with serializer.data['name'] & ...
        # print(serializer.data['name'])
        # print(serializer.data['familyName'])
        # print(serializer.data['phoneNumber'])
        # print(serializer.data['id'])

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CommandView(mixins.CreateModelMixin, generics.ListAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerilizer

    def perform_create(self, serializer):
        serializer.save()
        parrot_command.publish('%s,%s'%(serializer.data['commandName'],serializer.data['param']))
        # You can acces owner & commandName & id & param
        # with serializer.data['name'] & ...
        # print(serializer.data['owner'])
        # print(serializer.data['commandName'])
        # print(serializer.data['param'])
        # print(serializer.data['id'])

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CommandsOfUserView(generics.ListAPIView):
    serializer_class = CommandSerilizer
    def get_queryset(self):
        queryset = Command.objects.filter(owner__id=self.kwargs['pk'])
        return queryset
