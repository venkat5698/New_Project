
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee



from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def dashboardpage(request):
    return render(request, '../templates/index.html')
def layoutpage(request):
    return render(request, '../templates/layout-static.html')
def light(request):
    return render(request, '../templates/layout-sidenav-light.html')
def chart(request):
    return render(request, '../templates/charts.html')
def table(request):
    return render(request, '../templates/tables.html')


def add_item(request):
    if request.method == 'POST':
        # Extract form data using the correct 'name' attributes from the template
        employeename = request.POST.get('employeename')
        employeeid = request.POST.get('employeeid')
        assetid = request.POST.get('assetid')
        gender = request.POST.get('gender')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        try:
            # Assuming the Employee model is defined with appropriate fields and datatypes
            item = Employee(
                employeename=employeename,
                employeeid=employeeid,
                assetid=assetid,
                gender=gender,
                start_date=start_date,
                end_date=end_date,
            )
            item.save()
            messages.success(request, "Employee Details Added Successfully")
            # Redirect to the same page to clear the form after successful save
            return redirect('add_item')
        except Exception as e:
            # In case of any error during saving the data
            messages.error(request, f"Error: {e}")

    # If the request method is not POST, just render the template without doing anything.
    items = Employee.objects.all()
    return render(request, 'tables.html',  {'items': items})