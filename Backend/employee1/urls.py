from django.urls import path
from . import views
from .views import EmployeeDelete


urlpatterns = [
     path('', views.apiOverview, name="api-overview"),
     path('EmployeeList/', views.EmployeeList, name="employee-list"),
     path('EmployeeDelete/<str:pk>/',EmployeeDelete.as_view(), name="delete"),
]