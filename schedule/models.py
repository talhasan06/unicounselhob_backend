from django.db import models
from student.models import Student
from teacher.models import Teacher,AvailableTime

STATUS = [
    ('Completed','Completed'),
    ('Pending','Pending'),
    ('Running','Running'),
]

TYPES = [
    ('Offline','Offline'),
    ('Online','Online'),
]

class Schedule(models.Model):
    student = models.ForeignKey(Student,on_delete = models.CASCADE)
    teacher = models.ForeignKey(Teacher,on_delete = models.CASCADE)
    schedule_status = models.CharField(choices = STATUS,max_length = 10,default = "Pending")
    schedule_types = models.CharField(choices = TYPES,max_length = 10)
    description = models.TextField()
    time = models.ForeignKey(AvailableTime,on_delete = models.CASCADE)
    cancel = models.BooleanField(default = False)

    