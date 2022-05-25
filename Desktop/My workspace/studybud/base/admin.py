from django.contrib import admin
from django.contrib.auth.models import User
# Register your models here.
from .models import Message, Room, Topic
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)


