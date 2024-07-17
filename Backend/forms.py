from django import forms
from django.forms import ModelForm
from .models import Director, Movie


class DirectorForm(ModelForm):


    class Meta:

        COUNTRY_OPTIONS = (
            'Argentina',
            'Canada',
            'France',
            'Germany',
            'Italy',
            'Japan',
            'Mexico',
            'Spain',
            'United Kingdom',
            'United States',
        )

        model = Director
        fields = ['name', 'birthday', 'country']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-input',
                                           'required':True,
                                           'placeholder':'Name'}),
            'birthday': forms.SelectDateWidget(attrs={'type': 'date'}),
            'country': forms.Select(attrs={'class':'form-input',
                                           'required':True},
                                    choices=COUNTRY_OPTIONS)
        }
