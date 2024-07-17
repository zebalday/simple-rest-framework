from django.shortcuts import render
from django.views.generic import TemplateView
from Backend.models import Director, Movie
from Backend.forms import DirectorForm


class Index(TemplateView):

    def get(self, request):
       return render(request, template_name="Frontend/index.html")
    

class NewDirector(TemplateView):

    def get(self, request):

        form = DirectorForm()
        
        return render(request, 
                      template_name="Frontend/add_director.html", 
                      context={'form':form})
        