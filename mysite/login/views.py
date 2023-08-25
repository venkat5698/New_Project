from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Employee
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
#from .forms import EmployeeForm

def loginpage(request):
    return render(request,'../templates/login.html')
def forgotpasswordpage(request):
    return render(request,'../templates/password.html')
def registerpage(request):
    print("new")
    return render(request,'../templates/register.html')
#
# def add_item(request):
#     if request.method == 'POST':
#         # Extract form data using the correct 'name' attributes from the template
#         employeename = request.POST.get('employeename')
#         employeeid = request.POST.get('employeeid')
#         assetid = request.POST.get('assetid')
#         gender = request.POST.get('gender')
#         start_date = request.POST.get('start_date')
#         end_date = request.POST.get('end_date')
#
#         try:
#             # Assuming the Employee model is defined with appropriate fields and datatypes
#             item = Employee(
#                 employeename=employeename,
#                 employeeid=employeeid,
#                 assetid=assetid,
#                 gender=gender,
#                 start_date=start_date,
#                 end_date=end_date,
#             )
#             item.save()
#             messages.success(request, "Employee Details Added Successfully")
#             # Redirect to the same page to clear the form after successful save
#             return redirect('add_item')
#         except Exception as e:
#             # In case of any error during saving the data
#             messages.error(request, f"Error: {e}")
#
#     # If the request method is not POST, just render the template without doing anything.
#     items = Employee.objects.all()
#     return render(request, 'tables.html',  {'items': items})



def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    return render(request, 'employee_detail.html', {'employee': employee})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})

def employee_update(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee_form.html', {'form': form})

def employee_delete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employee_confirm_delete.html', {'employee': employee})