from rest_framework import serializers
from adrf.serializers import Serializer
from account.models import User
from rest_framework.serializers import ValidationError

class RegisterSerializer(Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
