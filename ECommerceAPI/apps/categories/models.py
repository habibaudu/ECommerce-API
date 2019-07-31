from django.db import models
from ECommerceAPI.apps.department.models import Department


class Categories(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
