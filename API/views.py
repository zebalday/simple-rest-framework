from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from Backend.models import Director, Movie
from API.serializers import DirectorSerializer, MovieSerializer


class DirectorApiView(APIView):
    

    def get(self, request, format=None):

        query = Director.objects.all()
        directors = DirectorSerializer(query, many=True)

        return Response(data=directors.data, status=status.HTTP_200_OK)
    

class MovieApiView(APIView):

    
    def get(self, request, format=None):

        query= Movie.objects.all()
        movies = MovieSerializer(query, many=True)

        return Response(data=movies.data, status=status.HTTP_200_OK)


class DirectorViewSets(ModelViewSet):


    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class MovieViewSets(ModelViewSet):


    queryset = Movie.objects.all()
    serializer_class = MovieSerializer





