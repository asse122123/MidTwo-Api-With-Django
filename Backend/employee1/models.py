from django.db import models

# Create your models here.
# from django.db import models

# Create your models here.
# from django.db import models
#from django.db import models
class Employee(models.Model):
    firstName = models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    EmployeeSalary=models.CharField(max_length=10)

    objects = models.Manager()
    def __str__(self):
        return self.firstName
     