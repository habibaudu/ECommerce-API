from django.db.models import Q
from rest_framework.serializers import (ValidationError, EmailField,
                                        CharField, ModelSerializer, Serializer)
from rest_framework import exceptions
from ECommerceAPI.apps.validator import validate_mobile_number
from ECommerceAPI.apps.authentication.models import User
from django.contrib.auth import authenticate


class LoginSerializer(ModelSerializer):
    email = EmailField(label="Email Address", required=False, allow_blank=True)
    mobile_number = CharField(required=False, allow_blank=True)
    token = CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ["mobile_number", "email", "password", "token"]
        extra_kwargs = {"password": {"write_only":  True}}

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        mobile_number = data.get("mobile_number", None)
        password = data["password"]
        if not email and not mobile_number:
            raise ValidationError("An email or a mobile_number \
                is required to login")

        user = User.objects.filter(
            Q(email=email) |
            Q(mobile_number=mobile_number)
        ).distinct()
        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError("No user with given email or mobile number")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Invalid Credentials please try again")
        return {
            'email': user_obj.email,
            'mobile_number': user_obj.mobile_number,
            'token': user_obj.token
        }


class RegisterSerializer(ModelSerializer):
    email2 = EmailField(label="Confirm Email")
    token = CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ["id", "mobile_number", "email", "email2",
                  "password", "token"]
        extra_kwargs = {"password": {"write_only":  True}}

    def validate(self, data):
        mobile_number = data.get("mobile_number", None)
        password = data.get("password", None)
        passlen = password.split()
        if len(passlen) < 8:
            raise ValidationError("password must be atleat 8 characters long")
        validate_mobile_number(mobile_number)
        email1 = data.get("email", None)
        email2 = data.get("email2", None)
        if email1 != email2:
            raise ValidationError("Both Emails must match")
        return data

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        mobile_number = validated_data["mobile_number"]

        user_obj = User(email=email, mobile_number=mobile_number)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data
