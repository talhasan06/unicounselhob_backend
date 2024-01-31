from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.
class ScheduleViewset(viewsets.ModelViewSet):
    queryset = models.Schedule.objects.all()
    serializer_class = serializers.ScheduleSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        student_id = self.request.query_params.get('patient_id')
        teacher_id = self.request.query_params.get('teacher_id')

        if student_id:
            queryset = queryset.filter(student_id = student_id)
        elif teacher_id:
            queryset = queryset.filter(teacher_id = teacher_id)
        return queryset