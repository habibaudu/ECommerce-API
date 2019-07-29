from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ECommerceAPI.apps.department.serializer import DepartmentSerializer
from ECommerceAPI.apps.department.models import Department
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly
)


class DepartmentView(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = DepartmentSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response({"error": "could not create department"}, status=400)

    def get(self, request):
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data, status=200)


class DepartmentDetailView(APIView):
    def get(self, request, id=None):
        department_instance = get_object_or_404(Department, pk=id)
        serializer = DepartmentSerializer(department_instance)
        return Response(serializer.data, status=200)

    def patch(self, request, id=None):
        data = request.data
        instance = get_object_or_404(Department, pk=id)
        serializer = DepartmentSerializer(instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, id=None):
        instance = get_object_or_404(Department, pk=id)
        instance.delete()
        return Response({"message": "department has been deleted"})
