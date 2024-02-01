from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AvailableTime(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    image = models.ImageField(upload_to="teacher/images/")
    course_name = models.CharField(max_length=100)
    available_time = models.ManyToManyField(AvailableTime)
    mobile_no = models.CharField(max_length=12)

    @property
    def full_name(self):
        return self.user.get_full_name()

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"