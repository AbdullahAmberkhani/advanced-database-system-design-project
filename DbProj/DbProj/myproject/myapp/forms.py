# myapp/forms.py
from django import forms
from .models import Employee, Position

class EmployeeForm(forms.ModelForm):
    """
    POSITION_CHOICES = [
        ('CEO', 'CEO'),
        ('CTO', 'CTO'),
        ('COO', 'COO'),
        ('CFO', 'CFO'),
    ]

    position = forms.ChoiceField(choices=POSITION_CHOICES)
    """

    class Meta:
        model = Employee
        fields = ['employee_name', 'age', 'contact_number', 'city']

class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['position', 'salary']
