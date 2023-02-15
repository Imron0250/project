from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('task', TaskViewRouter)
router.register('task_name', TaskNameRouter)