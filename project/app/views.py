from django.shortcuts import render

# Create your views here.
from .models import Student
from django.http import HttpResponse

# all_data=Student.objects.all()

# print(all_data)




def home(request):
    # data=Student.objects.all()
    # data1=data.values()
    # return HttpResponse(data1)
    # print(data)
    # return HttpResponse(data)


#filter()
    # data=Student.objects.filter(stu_city='bhopal')
    # data1=data.values()
    # return HttpResponse(data1)


#exclude()
    # data=Student.objects.exclude(stu_city='bhopal')
    # data1=data.values()
    # return HttpResponse(data1)

#order_by()
    # data=Student.objects.order_by('stu_city')#in assending order
    # data1=data.values()
    # return HttpResponse(data1)

    # data=Student.objects.order_by('-stu_city')#in decending order
    # data1=data.values()
    # return HttpResponse(data1)

    # data=Student.objects.order_by('?')#it will arrange in random order each time you refersh server order
    # data1=data.values()
    # return HttpResponse(data1)

    # data=Student.objects.order_by('stu_name')#in assending order names
    # data1=data.values()
    # return HttpResponse(data1)

#reverse()
    # data=Student.objects.order_by('id').reverse()#accordiing to id it will reverse
    # data=Student.objects.order_by('id').reverse()[:2]#first 3 entries
    # data1=data.values()
    # return HttpResponse(data1)

    #values()=>it will provides the dict formated value
    # data=Student.objects.values()#in assending order
    # # data1=data.values()
    # data=Student.objects.values('stu_name','stu_city')#in assending order

    # return HttpResponse(data)

    #values_list(*fields,flat=False,named=false)=>it will provide the value in tuple format

    # data=Student.objects.values_list()#in assending order
    # data=Student.objects.values_list('id','stu_name')#in assending order
    data=Student.objects.values_list('id','stu_name',named=True)#in assending order

    return HttpResponse(data)



    
    
 


    

