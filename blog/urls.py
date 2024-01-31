from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router = DefaultRouter()

router.register('',views.BlogViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('<int:pk>/', views.BlogDetailView.as_view({'get': 'blog_details'}))
]
