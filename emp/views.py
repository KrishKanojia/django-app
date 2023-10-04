from django.shortcuts import render,redirect
from django.http import HttpResponse
from emp.models import Emp

# Create your views here.
def emp_home(request):
    emps = Emp.objects.all()
    data = {
        "emps":emps
    }
    return render(request,"emp/home.html",data)


def add_emp(request):
    if request.method == "POST":

        # Data Fetch
        emp_name = request.POST.get("emp_name")
        emp_id = request.POST.get("emp_id")
        emp_phone = request.POST.get("emp_phone")
        emp_address = request.POST.get("emp_address")
        emp_working = request.POST.get("emp_working") 
        emp_department = request.POST.get("emp_department")


        print("Emp is ",emp_name)
        # Create model object and set the data
        e = Emp()
        e.name = emp_name
        e.emp_Id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department

        if emp_working is None:
            e.working = False
        else: 
            e.working = True

        # save the object
        e.save()
        # Prepare the message


        print("Data is coming")
        return redirect("/emp/home/")
    return render(request,"emp/add_emp.html",{})


def delete_emp(request,emp_id):
    e = Emp.objects.get(id=emp_id)
    print("Emp is ",emp_id)
    e.delete()
    return redirect("/emp/home/")


def update_emp(request,emp_id):
    e = Emp.objects.get(id=emp_id)
    return render(request,"emp/update_emp.html",{
        "emp" : e
    })


def do_update(request,emp_id):
    
    if request.method == "POST":
        emp = Emp.objects.get(id=emp_id)
        emp.name = request.POST.get("emp_name")
        emp.emp_Id = request.POST.get("emp_id")
        emp.phone = request.POST.get("emp_phone")
        emp.address = request.POST.get("emp_address")
        emp.department = request.POST.get("emp_department")

        if request.POST.get("emp_working") is None:
            emp.working = False
        else: 
            emp.working = True

        emp.save()
    return redirect("/emp/home/")