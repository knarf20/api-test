from rest_framework import routers
from .api import UserViewSet, UserViewSetOne
from django.urls import path

router = routers.DefaultRouter()

router.register('api/v1/users', UserViewSet, 'users')
router.register('', UserViewSetOne, 'oneUser')
urlpatterns = router.urls