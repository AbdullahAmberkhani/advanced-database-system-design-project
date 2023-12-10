# myapp/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, Position
from .forms import EmployeeForm, PositionForm

def add_data(request):
    if request.method == 'POST':
        # Create instances of EmployeeForm and PositionForm with the submitted data
        employee_form = EmployeeForm(request.POST)
        position_form = PositionForm(request.POST)

        # Check if both forms are valid
        if employee_form.is_valid() and position_form.is_valid():
            # Save Employee instance to get the primary key
            employee_instance = employee_form.save()

            # Create a Position instance with the linked Employee instance
            position_instance = position_form.save(commit=False)
            position_instance.employee = employee_instance
            position_instance.save()

            # Redirect to a success page or another appropriate page
            # return redirect('/view')  # Change 'success_page' to your actual success page URL
            return view_data(request)

    else:
        # If it's not a POST request, create empty forms
        employee_form = EmployeeForm()
        position_form = PositionForm()

    return render(request, 'add_data.html', {'employee_form': employee_form, 'position_form': position_form})

def modify_data(request, employee_id):    
    # Fetch the existing Employee instance using get_object_or_404
    employee = get_object_or_404(Employee, employee_id=employee_id)

    # Fetch the associated Position instance (if it exists)
    try:
        position = employee.position
    except Position.DoesNotExist:
        position = None

    if request.method == 'POST':
        # Create instances of EmployeeForm and PositionForm with the submitted data
        employee_form = EmployeeForm(request.POST, instance=employee)
        position_form = PositionForm(request.POST, instance=position)

        # Check if both forms are valid
        if employee_form.is_valid() and position_form.is_valid():
            # Save Employee instance
            employee_form.save()

            # Save Position instance
            if position:
                position_form.save()

            # Redirect to a success page or another appropriate page
            return view_data(request)

    else:
        # If it's not a POST request, create forms populated with existing data
        employee_form = EmployeeForm(instance=employee)
        position_form = PositionForm(instance=position)

    return render(request, 'modify_data.html', {'employee_form': employee_form, 'position_form': position_form, 'employee': employee})

def delete_data(request, employee_id):
    # Fetch the existing Employee instance using get_object_or_404
    employee = get_object_or_404(Employee, employee_id=employee_id)

    # Delete the Employee instance
    employee.delete()

    # Redirect to a success page or another appropriate page
    return view_data(request)

def view_data(request):
    # Fetch all Employee instances and pass them to the template
    employees = Employee.objects.all()

    return render(request, 'view_data.html', {'employees': employees})
