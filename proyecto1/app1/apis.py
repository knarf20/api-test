from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Todo
from .serializers import TodoSerializer

""" Aca estamos usando APIView ya que nos brinda la opcion de trabajar con los metodos HTTP GET, POST, PUT, DELETE
Entonces cuando usemos esta view en nuestras rutas de forma automatica sabra cuales son los metodos que debe exponer.
En este caso en especifo solo vamos a disponibilizar/exponer los metodos GET, DELETE y POST
 """
class AllTodo(APIView):

    def get(self, request):
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def delete(self, request):
        Todo.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def post(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
