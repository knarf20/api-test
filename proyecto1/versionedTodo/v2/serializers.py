from rest_framework import serializers
from app1.models import Todo
from users.models import User
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        author = serializers.SlugRelatedField(queryset=User, slug_field='author', required=False)
        read_only_fields = 'created_at', 'done_at', 'updated_at', 'deleted_at'