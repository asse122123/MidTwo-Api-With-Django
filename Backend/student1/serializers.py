from rest_framework import serializers
from .models import Student
from .models import Teacher
from .models import Employee


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

        