from rest_framework import viewsets, mixins
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from . import models
from . import serializers


# Create your views here.

class TodoItemViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    renderer_classes = [
        JSONRenderer,
        TemplateHTMLRenderer
    ]

    serializer_class = serializers.TodoItemSerializer
    queryset = models.TodoItem.objects.filter(is_done=False)

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.template_name = 'todo_item_list.html'
        return response
