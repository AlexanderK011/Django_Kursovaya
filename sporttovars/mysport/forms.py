from django import forms
from django.contrib.auth.forms import UserCreationForm

from mysport.models import Feedback,User



class UserRegForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name','number_phone','address','postal_index']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['email','text']



