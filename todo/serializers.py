from django.contrib.auth.models import User
from rest_framework import serializers
from . import models


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoItem
        fields = '__all__'
