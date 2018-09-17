from django.contrib import admin
from .models import Log
from .models import Command
# Register your models here.
admin.register(Log)
admin.register(Command)