from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from mysport.models import Profile


class UserRegForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class profileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name','last_name','number_phone', 'address','postal_index']


