from django.shortcuts import render
from adrf.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from account.serializers import RegisterSerializer
from django.db import IntegrityError
from account.models import User

# Create your views here.
class RegisterView(APIView):
    permission_classes = [AllowAny]

    async def post(self, request, *args, **kwargs):
        request.data["password"] = make_password(request.data["password"])
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User()
                user.email = serializer.validated_data["email"]
                user.password = make_password(serializer.validated_data["password"])
                await user.asave()
                return Response(
                    {"message": "User registered successfully.", "user_id": user.id},
                    status=status.HTTP_201_CREATED,
                )
            except IntegrityError:
                return Response(
                    {"error": "A user with this email already exists."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
