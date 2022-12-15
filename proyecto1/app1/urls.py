# ...
from django.urls import re_path, include
from versionedTodo.v1.router import api_urlpatterns as api_v1
from versionedTodo.v2.router import api_urlpatterns as api_v2
from rest_framework import routers
from django.urls import path

router = routers.DefaultRouter()
# ....

urlpatterns = [
    re_path(r'^api/v1/', include(api_v1)),
    re_path(r'^api/v2/', include(api_v2)),
    #path('api/v2/', include(api_v2)),

]

urlpatterns += router.urls