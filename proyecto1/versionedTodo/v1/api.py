from app1.models import Todo
from .serializers import TodoSerializer
from rest_framework import status
from rest_framework.response import Response
from .pagination import StandardResultsSetPagination
from rest_framework import viewsets, filters 
from rest_framework.throttling import UserRateThrottle

class TodoViewSet(viewsets.ModelViewSet):
     queryset = Todo.objects.all()
     serializer_class = TodoSerializer
     pagination_class = StandardResultsSetPagination
     filter_backends = [filters.SearchFilter, filters.OrderingFilter]

     search_fields = ['title', 'body']
     ordering = ('-id')
     #throttle_classes = [UserRateThrottle]

     #este nombre escope debe hacer match con algunos de los scopes definidos en DEFAULT_THROTTLE_RATES
     throttle_scope = 'get'