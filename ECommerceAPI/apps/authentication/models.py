import jwt
from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        PermissionsMixin, BaseUserManager)
from datetime import datetime, timedelta
from django.conf import settings
from django.core.mail import send_mail


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        if not email:
            raise ValueError('Email must be provided')
        user = self.model.objects.filter(email=email).first()
        if user:
            raise ValueError(
                "User with email {email} already exists".format(email=email)
            )
        mobile_number = extra_fields.get("mobile_number")
        user_mobile_number = \
            self.model.objects.filter(mobile_number=mobile_number).first()
        if user_mobile_number:
            raise ValueError(
                "User with mobile number {mobile_number} "
                "already exists".format(mobile_number=mobile_number)
            )
        email = self.normalize_email(email)
        user = self.model(email=email,
                          mobile_number=mobile_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser must be True')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=100, null=True, unique=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    profile_image = models.URLField(default='profile.png')
    date_joined = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def get_full_name(self):

        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')
