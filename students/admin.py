# from django.contrib import admin

# # Register your models here.
from django.contrib import admin
from .models import Course, Student, Marks, Attendance

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Marks)
admin.site.register(Attendance)