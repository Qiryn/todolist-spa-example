from rest_framework import serializers
from . import models


class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TodoItem
        fields = '__all__'


#class TodoItemSerializer(serializers.Serializer):
#    name = serializers.CharField(max_length=200)
#    is_done = serializers.BooleanField()
