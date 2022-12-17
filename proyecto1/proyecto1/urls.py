"""proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from app1 import apis
from rest_framework import routers

router = routers.DefaultRouter()

#si queremos sobre escribir nuestras errors view por defecto mas info https://docs.djangoproject.com/en/dev/topics/http/views/#customizing-error-views
#handler500 = 'app1.views.page_not_found_view'

#router.register('api/v1/todo', apis.TodoViewSetCustom, 'todosCustom')
#router.register('api/v2/todo', apis.TodoViewSet, 'todos')

"""
 como se comento en el apis.py no cuando creamos una ruta que esta siendo uso de 
APIView no es necesario indicarle de forma explicita el metedo HTTP debido
a que eso se mapea de forma automatica con los metodos que definamos dentro de la VIEW
"""
urlpatterns = [
    #path("admin/", admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('app1.urls')),

]
urlpatterns += router.urls
