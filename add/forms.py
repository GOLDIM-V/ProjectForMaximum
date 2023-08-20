from django import forms
from .models import Advert
from django.core.exceptions import ValidationError

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

    def clean_title(self):
        title = self.cleaned_data['title']
        if title[0] == '?':
            raise ValidationError('Заголовок не может начинаться с "?"')
        return title