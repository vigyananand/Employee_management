from django.shortcuts import render,HttpResponse
from .models import Employee,Role,Department
from datetime import datetime
from django.db.models import Q

def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request, 'all_emp.html',context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = eval(request.POST['phone'])
        salary = eval(request.POST['salary'])
        bonus = eval(request.POST['bonus'])
        dept = eval(request.POST['dept'])
        role = eval(request.POST['role'])
        # location = request.POST['location']
        hire_date = request.POST['hire_date']

        new_emp = Employee(first_name=first_name, last_name=last_name, phone=phone, salary=salary, bonus=bonus, dept_id =dept, role_id =role, hire_date= datetime.now())
        new_emp.save()
        return HttpResponse('Employee added successfully')
    elif request.method=='GET':
    
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('wrong details')


def remove_emp(request, emp_id = 0):
    if emp_id:
        try:
            emp_to_be_removed= Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("please enter a valid EMP ID")

    emps=Employee.objects.all()
    context = {
        'emps':emps
    }

    return render(request, 'remove_emp.html',context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps= Employee.objects.all()
        if name:
            emps = emps.filter(Q(first_name__icontains = name) | Q(last_name__icontains = name))

            # icontains ka kam use first ya last ya middle me bhi ek do word mil jate hai to wo sbko filter
            # karke nikal deta hai..basically ye check karta hai ki wo word usme khi hai ya ni
            # for Q fn go to SS section

        if dept:
            emps = emps.filter(dept__name__icontains = dept)
        if role:
            emps = emps.filter(role__name__icontains = role)

        context={
            'emps':emps
        }
        return render(request, 'all_emp.html', context)

    elif request.method == 'GET':
        return render(request, 'filter_emp.html')
    else:
        return HttpResponse('invalid Exception occured')
# Create your views here.
