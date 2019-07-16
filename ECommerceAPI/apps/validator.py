import re
from ECommerceAPI.apps.department.models import Department
from rest_framework.serializers import (ModelSerializer, ValidationError)


def Validator_inputs(validated_data):
        fields = ["name", "description"]
        if "name" not in validated_data:
            fields.remove("name")
        for key in fields:
            string_regex = re.search(r"[^a-zA-Z.',\-\s]+", validated_data[key])
            if string_regex is not None:
                msg = f"{key} can contain only alphabets"
                raise ValidationError(msg)
        if 'name' in validated_data:
            department_qs = Department.objects.filter(
                            name=validated_data["name"])
            if department_qs.exists():
                msg = f"A department named '{validated_data['name']}' \
                        already exist."
                raise ValidationError(msg)
            return validated_data
        return validated_data
