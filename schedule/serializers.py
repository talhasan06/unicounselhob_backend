from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class ScheduleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False)
    student = serializers.StringRelatedField(many = False)
    teacher = serializers.StringRelatedField(many = False)
    
    class Meta:
        model = models.Schedule
        fields = "__all__"