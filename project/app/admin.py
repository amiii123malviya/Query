from django.contrib import admin
from .models import Student
# Register your models here.

# admin.site.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display=('id','stu_name','stu_email','stu_city')
admin.site.register(Student,StudentAdmin)