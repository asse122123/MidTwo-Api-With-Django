from django.urls import path
from . import views
from .views import TeacherDelete


urlpatterns = [
     path('', views.apiOverview, name="api-overview"),
     path('TeacherList/', views.TeacherList, name="Teacher-list"),
    path('TeacherDelete/<str:pk>/',TeacherDelete.as_view(), name="delete")
]