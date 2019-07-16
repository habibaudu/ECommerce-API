from django.urls import path, include
from ECommerceAPI.apps.department import views

urlpatterns = [
    path("departments/", views.DepartmentView.as_view()),
    path("department/<int:id>/", views.DepartmentDetailView.as_view())
]
