from django.urls import path

from .views import HomeView, EmployeeView, EmployeeFormView

urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("employeeform", EmployeeFormView.as_view(), name='employeeform'),
    path("employee", EmployeeView.as_view(), name='employee')
]