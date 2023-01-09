from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import RegistrationSerializer, LoginSerializer
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken


class RegistrationView(APIView):
    def post(self, request):
        serialzer = RegistrationSerializer(
            data=request.data)
        serialzer.is_valid(raise_exception=True)
        serialzer.save()
        return Response('Аккаунт успешно создан', status=201)

class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer