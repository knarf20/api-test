from rest_framework import serializers
from .models import Todo
from users.models import User
class TodoSerializer(serializers.ModelSerializer):
    author  = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    class Meta:
        model = Todo
        fields = ('title', 'body', 'created_at', 'done_at', 'updated_at', 'deleted_at', 'status', 'author')
