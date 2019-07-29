from ECommerceAPI.apps.authentication.models import User
from ECommerceAPI.apps.department.models import Department
from rest_framework.test import APITestCase, APIClient
from rest_framework.status import HTTP_200_OK
import json


class BaseConfiguration(APITestCase):

    def setUp(self):
        self.csrf_client = APIClient(enforce_csrf_checks=True)
        self.department = {
            "id": 1,
            "name": "Regional",
            "description": "awesome department, gets things done"
        }
        self.new_user = {
            "email": "habib@gmail.com",
            "mobile_number": "08012706429",
            "password": "Password123"
        }
        self.login_user = {
            "email": "habib@gmail.com",
            "password": "Password123"
        }
        self.user = self.register_user(self.new_user)
        self.token = self.user_login()
        self.dept = self.create_department()

    def register_user(self, user):
        """
        register a new user
        """
        email = user["email"]
        mobile_number = user["mobile_number"]
        password = user["password"]
        user = User.objects.create_user(
            email=email, mobile_number=mobile_number, password=password)
        user.save()
        return user.token

    def user_login(self):
        """
        Log in registered user and return a token
        """
        response = self.client.post("/api/v1/auth/login/",
                                    data=self.login_user,
                                    format='json')
        return response

    def create_department(self):
        return Department.objects.create(
                                         name="Reginall", 
                                         description="a department")
