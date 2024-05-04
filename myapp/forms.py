# forms.py
from django import forms
from .models import student_details
from .models import CustomUser

class StudentForm(forms.ModelForm):
    class Meta:
        model = student_details
        fields = ['name', 'fav_language']







class SignUpForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'