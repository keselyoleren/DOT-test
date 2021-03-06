from django.db import models
from rest_framework import serializers

from django.contrib.auth.models import User

class UserSerialize(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']