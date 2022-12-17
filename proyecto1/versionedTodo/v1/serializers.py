from rest_framework import serializers
from app1.models import Todo
from users.models import User

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'body', 'created_at', 'done_at', 'updated_at', 'deleted_at', 'status', 'author', 'username')
        read_only_fields = 'created_at', 'done_at', 'updated_at', 'deleted_at', 'username'