from django.urls import path
from ECommerceAPI.apps.authentication import views


urlpatterns = [
    path("auth/login/", views.LoginView.as_view(), name='login'),
    path("auth/register/", views.RegisterView.as_view(), name='register'),
]
