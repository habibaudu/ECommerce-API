from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from ECommerceAPI.apps.categories.serializer import CategoriesSerializer
from ECommerceAPI.apps.categories.models import Categories


class CategoriesView(APIView):
    def post(self, request):
        data = request.data
        serializer = CategoriesSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request):
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data, status=200)


class CategoriesViewDetails(APIView):
    def get(self, request, id=None):
        category_instance = get_object_or_404(Categories, pk=id)
        serializer = CategoriesSerializer(category_instance)
        return Response(serializer.data, status=200)

    def patch(self, request, id=None):
        data = request.data
        category = get_object_or_404(Categories, pk=id)
        serializer = CategoriesSerializer(category, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

    def delete(self, request, id=None):
        category_instance = get_object_or_404(Categories, pk=id)
        category_instance.delete()
        return Response({"message": "Category deleted"})
