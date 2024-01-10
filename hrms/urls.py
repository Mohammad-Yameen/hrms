from django.urls import path

from .views import index, create_employee, get_employee

urlpatterns = [
    path("", index),
    path("create_employee", create_employee),
    path("get_employee", create_employee)
]