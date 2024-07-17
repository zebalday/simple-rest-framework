from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from Backend.models import Director, Movie
from Backend.forms import DirectorForm


class NewDirector(TemplateView):


    def post(self, request):
        pass

