from django import forms
from django.contrib.auth.forms import UserCreationForm,SetPasswordForm

from mysport.models import Feedback,User,Order


class UserRegForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name','number_phone','address','postal_index','city']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['email','text']


class UserPasswordChangeForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','number_phone','address','postal_index','city','email']

class OrderChangeForm(forms.ModelForm):
    STATUS_CHOICES = [
        ('На рассмотрении', 'На рассмотрении'),
        ('В пути', 'В пути'),
        ('Доставлен', 'Доставлен')
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES)
    deny_buy = forms.BooleanField(required=False)
    paid = forms.BooleanField(required=False)
    note = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Order
        fields = ['deny_buy','paid','status','note']