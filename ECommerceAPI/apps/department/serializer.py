import re
from rest_framework.serializers import (ModelSerializer, ValidationError)
from ECommerceAPI.apps.department.models import Department
from ECommerceAPI.apps.validator import Validator_inputs


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        fields = ["id", "name", "description"]      

    def create(self, validated_data):
        data = Validator_inputs(validated_data)
        return Department.objects.create(**data)

    def update(self, instance, validated_data):
        data = Validator_inputs(validated_data)
        instance.name = data.get("name", instance.name)
        instance.description = data.get("description", instance.description)
        instance.save()
        return instance
