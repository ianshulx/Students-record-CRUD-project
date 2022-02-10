from django.contrib import admin
from .models import Student_data



@admin.register(Student_data)
class StudentdataModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'first_name', 'dob', 'gender', 'address', 'pin', 'course', 'mobile']


