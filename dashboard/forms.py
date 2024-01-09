from django import forms
from food.models import *

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields = "__all__"
        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control'}),

        }

class UserForm(forms.ModelForm):
    model = Customer
    field = "__all__"
    widjets = {
        "first_name": forms.TextInput(attrs={'class': 'form-control'}),
        "last_name": forms.TextInput(attrs={'class': 'form-control'}),
        "phone_number": forms.TextInput(attrs={'class': 'form-control'}),
    }