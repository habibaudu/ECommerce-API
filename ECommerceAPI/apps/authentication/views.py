from ECommerceAPI.apps.authentication.serializer import(LoginSerializer,
                                                        RegisterSerializer)
from ECommerceAPI.apps.authentication.renderers import UserJSONRenderer
from django.contrib.auth import login as django_login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import(HTTP_200_OK,
                                  HTTP_400_BAD_REQUEST, HTTP_201_CREATED)
from ECommerceAPI.apps.authentication.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class RegisterView(APIView):
    permission_classes = [AllowAny]
    renderer_classes = (UserJSONRenderer,)
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=HTTP_201_CREATED)
