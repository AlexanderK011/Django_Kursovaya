from django import forms

# PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
from mysport.models import Order,AnonymCustomer


class CartAddProductForm(forms.Form):
    # quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class OrderCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].disabled = True
        self.fields['anonymuser'].disabled = True

    class Meta:
        model = Order
        fields = ['user','anonymuser']


class AnonOrd(forms.ModelForm):
    class Meta:
        model = AnonymCustomer
        fields = ['id','first_name','last_name','number_phone','city','address','postal_index']