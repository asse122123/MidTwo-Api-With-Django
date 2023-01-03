from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
#from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer
from .models import Student




# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'student-list' : '/student-list/',
        'Create' : '/student-create/',
        'Detail' : '/student-list/<str:pk>/',
        'Update' : '/student-update/<str:pk>/',
        'Delete' : '/student-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def studentList(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many = True)
    return Response(serializer.data)
    
class StudentDelete(generics.DestroyAPIView):
  queryset=Student.objects.all()
  Serializer_class = StudentSerializer


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'teacher-list' : '/teacher-list/',
        'Create' : '/teacher-create/',
        'Detail' : '/teacher-list/<str:pk>/',
        'Update' : '/teacher-update/<str:pk>/',
        'Delete' : '/teacher-delete/<str:pk>/'
    }
    return Response(api_urls)



@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'employee-list' : '/employee-list/',
        'Create' : '/employee-create/',
        'Detail' : '/employee-list/<str:pk>/',
        'Update' : '/employee-update/<str:pk>/',
        'Delete' : '/employee-delete/<str:pk>/'
    }
    return Response(api_urls)


# @api_view(['POST'])
# def createView(request):
#     serializer = StudentSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#     return Response(serializer.data)

# @api_view(['POST'])
# def updateView(request,pk):
#     student = Student.objects.get()
#     serializer = StudentSerializer(student, data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)    


# # Create your views here.
# # Create your views here.
