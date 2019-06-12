from django.shortcuts import render, redirect

# Create your views here.
import employee
from employee.models import Employee


def index(request):
    emp = Employee.objects.all()
    return render(request,'test.html', {'emp':emp})




def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/index")


