from django.shortcuts import render

# Create your views here.
from .models import Student
from django.http import HttpResponse

# all_data=Student.objects.all()

# print(all_data)




def home(request):
    data=Student.objects.all()
    data1=data.values()
    return HttpResponse(data1)
    print(data)
    # return HttpResponse(data)
