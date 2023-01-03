from django.urls import path
from . import views
from .views import StudentDelete


urlpatterns = [
     path('', views.apiOverview, name="api-overview"),
     path('student-list/', views.studentList, name="student-list"),
     path('StudentDelete/<str:pk>/',StudentDelete.as_view(), name="delete")
]