from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ('title', 'body', 'created_at', 'done_at', 'updated_at', 'deleted_at', 'status', 'author')
