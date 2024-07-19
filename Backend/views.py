from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from Backend.models import Director, Movie
from Backend.forms import DirectorForm, MovieForm


class NewDirector(TemplateView):


    def post(self, request):
        
        try:
            form = DirectorForm(request.POST)
            
            if form.is_valid():
                name = form.cleaned_data["name"]
                birthday = form.cleaned_data["birthday"]
                country = form.cleaned_data["country"]

                Director(name=name, 
                         birthday=birthday, 
                         country=country).save()
                messages.success(request, f"New Director {name} added.")
        
        except Exception as e:
            print(e.__traceback__)
            messages.error(request, f"There was an error.")
            
        return redirect('Frontend:add-director')


class NewMovie(TemplateView):

    def post(self, request):

        try:
            form = MovieForm(request.POST)
            
            if form.is_valid():
                name = form.cleaned_data["name"]
                release_date = form.cleaned_data["release_date"]
                category = form.cleaned_data["category"]
                director = form.cleaned_data["director"]
                description = form.cleaned_data["description"]

                Movie(
                    name = name,
                    release_date = release_date,
                    category = category,
                    director = director,
                    description = description
                ).save()

                messages.success(request, f"New Movie {name} added.")

        except Exception as e:
            print(e.__traceback__)
            messages.error(request, f"There was an error.")

        return redirect('Frontend:add-movie')




