from rest_framework import serializers
from .models import  Log
from .models import Command
class LogSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('id','name', 'familyName', 'phoneNumber')
class CommandSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Command
        fields = ('id','owner','commandName', 'param')
