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
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"
        # widgets={
        #     "image":forms.FileInput(attrs={'class':'form-control'}),
        #     "title":forms.TextInput(attrs={'class':'form-control'}),
        #     "descriptions":forms.TextInput(attrs={'class':'form-control'}),
        #     "created":forms.TextInput(attrs={'class':'form-control'}),
        #     "category":forms.Select(attrs={'class':'form-control'}),
        # }