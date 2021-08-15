from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from todoapi.models import Todo

class TodoSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = ["id","title","completed","user"]
    
