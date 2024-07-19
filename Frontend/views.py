from django.shortcuts import render
from django.views.generic import TemplateView
from Backend.models import Director, Movie
from Backend.forms import DirectorForm, MovieForm


class Index(TemplateView):

    def get(self, request):
       return render(request, 
                     template_name="Frontend/index.html")
    

class NewDirector(TemplateView):

    def get(self, request):

        form = DirectorForm()
        directors = Director.objects.all().order_by('-birthday')
        
        return render(request, 
                      template_name="Frontend/add_director.html", 
                      context={'form':form,
                               'directors':directors})


class NewMovie(TemplateView):

    def get(self, request):

        form = MovieForm()
        movies = Movie.objects.all()
        
        return render(request, 
                      template_name="Frontend/add_movie.html", 
                      context={'form':form,
                               'movies':movies})