from django import forms
from django.forms import ModelForm
from .models import Links


class LinkForm(ModelForm):

    class Meta:
        model = Links
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'shortlink': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'link': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'user': forms.TextInput(attrs={
                'class': 'form-control', 'readonly': 'readonly'
            }),
        }





