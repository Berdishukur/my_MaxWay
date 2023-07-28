from django import forms
from .models import *
class CategoryyForm(forms.ModelForm):
    class Meta:
        model = Ctegory
        fields= "__all__"
        widgets = {
        "name":forms.TextInput(attrs={'class':'form-control'}),
        "created":forms.TextInput(attrs={'class':'form-control'})
        }