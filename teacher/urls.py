from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router = DefaultRouter()

router.register('list',views.TeacherViewset)
router.register('available_time',views.AvailableTimeViewset)

urlpatterns = [
    path('',include(router.urls))
]
