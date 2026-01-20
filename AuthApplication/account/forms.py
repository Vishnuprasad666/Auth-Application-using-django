from django import forms
from account.models import *
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","phone","username"]
        widgets={
            "first_name":forms.TextInput(attrs={"placeholder":"Enter First Name","class":"form-control"}),
            "last_name":forms.TextInput(attrs={"placeholder":"Enter Last Name","class":"form-control"}),
            "email":forms.EmailInput(attrs={"placeholder":"Enter Email ID","class":"form-control"}),
            "phone":forms.NumberInput(attrs={"placeholder":"Enter Phone Number","class":"form-control"}),
            "username":forms.TextInput(attrs={"placeholder":"Enter Userame","class":"form-control"}),
            "password1":forms.PasswordInput(attrs={"placeholder":"Enter Password","class":"form-control"}),
            "password2":forms.PasswordInput(attrs={"placeholder":"Re-Enter Password","class":"form-control"})
        }
        
class LoginForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=["owner"]