from django import forms
from .models import *
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= "__all__"
        widgets = {
        "name":forms.TextInput(attrs={'class':'form-control'}),
        "created":forms.TextInput(attrs={'class':'form-control'})
        }