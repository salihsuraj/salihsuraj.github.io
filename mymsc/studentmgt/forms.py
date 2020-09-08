from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class ExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password']
        widgets = {'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}),
                   'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
                   }