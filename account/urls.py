from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.UserRegistrationApiView.as_view(),name='register'),
    path('login/',views.UserLoginApiView.as_view(),name='login'),
    path('logout/',views.UserLogoutView.as_view(),name='logout'),
    path('active/<uid64>/<token>/',views.activate,name='active'),
]