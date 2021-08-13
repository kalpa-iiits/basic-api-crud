from EmployeeApp.models import Employee
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)