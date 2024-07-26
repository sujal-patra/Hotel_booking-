from django import forms
from .models import UserModel

class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput,required=True)

