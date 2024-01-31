from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class StudentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many = False)

    class Meta:
        model = models.Student
        fields = "__all__"