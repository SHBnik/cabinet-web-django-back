from django.db import models

# Create your models here.
class Log(models.Model):
    name = models.CharField(max_length=100)
    familyName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=100)

class Command(models.Model):
    owner = models.ForeignKey(Log, on_delete=models.CASCADE)
    commandName = models.CharField(max_length=100)
    param = models.IntegerField(blank=True,null=True)

