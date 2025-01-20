from django.contrib import admin
from .models import Student

@admin.register(Student)
class Student(admin.ModelAdmin):
    model = Student
    fields = ['__all__' ]