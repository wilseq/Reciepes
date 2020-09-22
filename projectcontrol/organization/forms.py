from django import forms
from .models import Employee, Students

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"