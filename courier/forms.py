from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User

# class RegisterId(UserCreationForm):
#     username = forms.CharField(max_length=250, required=True)
#     class Meta:
#         model = User
#         fields = ('username',)

class LoginForm(AuthenticationForm):
    username  = forms.CharField(max_length=200, label="Full Name", widget=forms.TextInput(attrs={"placeholder":'Enter Your Full Name'}))
    password = forms.CharField(max_length=255, label="Token ID", widget=forms.TextInput(attrs={"placeholder":'Enter Your Token id'}))
    
    class Meta:
        fields= ("password")