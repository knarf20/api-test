
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app1 import apis



urlpatterns = [
  path('todo', apis.AllTodo.as_view()),
  path('test1', apis.AllTodo.as_view()),
  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
