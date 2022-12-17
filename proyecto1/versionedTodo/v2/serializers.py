from rest_framework import serializers
from app1.models import Todo
from users.models import User
class TodoSerializer(serializers.ModelSerializer):
    author  = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='email')
    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = 'created_at', 'done_at', 'updated_at', 'deleted_at'