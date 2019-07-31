from rest_framework.serializers import (ModelSerializer, ValidationError)
from ECommerceAPI.apps.categories.models import Categories
from ECommerceAPI.apps.validator import Validator_inputs


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = ["id", "name", "description", "department_id"]
