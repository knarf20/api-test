from . import api
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'todo', api.TodoViewSetCustom, 'todosCustom')
router.register(r'users', api.TodoViewSetCustom, 'todosCustom')

api_urlpatterns = router.urls

