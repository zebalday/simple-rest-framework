from django import forms
from django.forms import ModelForm
from .models import Director, Movie
from django.contrib.admin.widgets import AdminDateWidget


class DateInput(forms.DateInput):
    input_type = 'date'


class DirectorForm(ModelForm):


    class Meta:

        COUNTRY_OPTIONS = {
            'AR':'Argentina',
            'CA':'Canada',
            'FR':'France',
            'GER':'Germany',
            'ITA':'Italy',
            'JPN':'Japan',
            'MX':'Mexico',
            'SPN':'Spain',
            'UK':'United Kingdom',
            'USA':'United States',
        }

        model = Director
        fields = ('name', 'birthday', 'country')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-input',
                                           'required':True,
                                           'placeholder':'Name'}),
            'birthday': DateInput(),
            'country': forms.Select(attrs={'class':'form-input',
                                           'required':True},
                                    choices=COUNTRY_OPTIONS)
        }
        labels = {
            'name': 'Name',
            'birthday':'Year of Birth',
            'country': 'Nationality'
        }


class MovieForm(ModelForm):
    
    
    class Meta:

        """ CATEGORY_OPTIONS = [
            'Horror',
            'Science Fiction',
            'Drama',
            'Action',
            'Thriller',
            'Documentary',
            'Romance',
            'Short',
        ] """
        CATEGORY_OPTIONS = {
            'Horror': 'Horror',
            'Science Fiction': 'Science Fiction',
            'Drama': 'Drama',
            'Action': 'Action',
            'Thriller': 'Thriller',
            'Documentary': 'Documentary',
            'Romance': 'Romance',
            'Short': 'Short',
        }

        model = Movie
        fields = ('name', 'release_date', 'category', 'director', 'description')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-input',
                                           'required':True,
                                           'placeholder':'Name'}),
            'release_date':DateInput(),
            'category':forms.Select(attrs={'class':'form-input',
                                           'required':True},
                                    choices=CATEGORY_OPTIONS),
            'director':forms.Select(attrs={'class':'form-input',
                                           'required':True}),
            'description':forms.Textarea(attrs={'class':'form-input',
                                           'required':True,
                                           'placeholder':'Movie plot'})

        }
        labels = {
            'name':'Movie Name',
            'release_date':'Release Date',
            'category':'Category',
            'director':'Movie Director',
            'description':False
        }