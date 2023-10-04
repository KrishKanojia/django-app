from django.http import HttpResponse
from django.shortcuts import render
from website.models import Student
import datetime

def home(request):
    isActive=True
    check = None
    if request.method == "POST":
        check = request.POST.get("Check")
        abc = request.POST["abc"]
        print("is check ",check, abc)

    date = datetime.datetime.now()
    name="LearnCodewithDurgesh"
    list_of_programs=[
        "WAP a print all prime numbers between 1 to 100",
        "WAP to print pascal triangle",
        "WAP to check prime number",
        "WAP to check even or odd"
        ]
    student ={
        'student_name': "Rahul",
        'school': "xyz",
        'city': "Karachi"

    }

    data = {
        'isActive': isActive,
       'name': name,
        'date':date,
        'list_of_programs': list_of_programs,
        'studentdata' : student
    }
    data_value ={}
    if check is not None:
        isActive = True
        new_std = Student(name=student['student_name'],college=student['school'],age=20,is_active=isActive)
        new_std.save()
        data_value = {
            "data" : new_std
        }
    
    else: isActive = False
    print("IsActive : ",isActive)
    print("Method is :{}".format(request.method))
    
    # return HttpResponse("<h1>Hello World</h1>" + str(time))
    return render(request,"home.html",data_value)


def about(request):
    # return HttpResponse("<h1>About Page</h1>")
    return render(request,"about.html",{})



def services(request):
    # return HttpResponse("<h1>Services Page</h1>")
    return render(request,"services.html",{})