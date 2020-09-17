from django.views.generic import TemplateView
from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication
from rest_framework.metadata import SimpleMetadata, BaseMetadata
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from . import models
from . import serializers


# Create your views here.


class TodoItemViewSet(viewsets.ModelViewSet):
    renderer_classes = [
        JSONRenderer,
        TemplateHTMLRenderer
    ]
    template_name = 'todo_item_list.html'
    serializer_class = serializers.TodoItemSerializer
    queryset = models.TodoItem.objects.filter(is_done=False)


class SwaggerUIView(TemplateView):
    template_name = 'swagger-ui/index.html'
