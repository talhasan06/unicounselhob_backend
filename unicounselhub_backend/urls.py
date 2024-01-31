
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from account import views
router = DefaultRouter()

router.register('users',views.UserListViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    path('schedule/',include('schedule.urls')),
    path('student/',include('student.urls')),
    path('teacher/',include('teacher.urls')),
    path('account/',include('account.urls')),
]

urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
