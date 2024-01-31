from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class TeacherSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many =False)
    available_time = serializers.StringRelatedField(many = True)

    class Meta:
        model = models.Teacher
        fields = "__all__"

class AvailableTimeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False)
    class Meta:
        model = models.AvailableTime
        fields = "__all__"
