from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

class TaskNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_name
        fields = ""