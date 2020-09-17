"""tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from rest_framework import routers
from rest_framework.renderers import JSONRenderer
from rest_framework.schemas import get_schema_view

from todo import views as todo_views
from quickstart import views as qs_views
from todo.views import SwaggerUIView

router = routers.DefaultRouter()
router.register('users', qs_views.UserViewSet)
router.register('groups', qs_views.GroupViewSet)
router.register('todoitems', todo_views.TodoItemViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),

    path('openapi', get_schema_view(
      title="TODO App",
      description="TODO Items App",
      version="1.0.0",
      renderer_classes=[JSONRenderer]
    ), name='openapi-schema'),

    path('swagger-ui',
         login_required(todo_views.SwaggerUIView.as_view(),
                        login_url='admin/login/'),
         name='swagger-ui'),

] + static(settings.STATIC_URL,
           document_root=settings.STATIC_ROOT)