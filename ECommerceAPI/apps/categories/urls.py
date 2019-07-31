from django.urls import path, include
from ECommerceAPI.apps.categories import views

urlpatterns = [
    path("categories/", views.CategoriesView.as_view()),
    path("category/<int:id>/", views.CategoriesViewDetails.as_view())
]
