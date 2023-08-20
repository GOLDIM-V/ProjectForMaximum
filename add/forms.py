from django import forms
from .models import Advert

class AdvertForm(forms.ModelForm):
    class Meta:
        model = Advert
        fields = ["title", "description", "price", 'image', "auction"]
        widgets = {
            'title': forms.TextInput(attrs={'class': "form-control form-control-lg"}),
            'description': forms.Textarea(attrs={'class': "form-control form-control-lg"}),
            'price': forms.NumberInput(attrs={'class': "form-control form-control-lg"}),
            'image': forms.FileInput(attrs={'class': "form-control form-control-lg"}),
        }