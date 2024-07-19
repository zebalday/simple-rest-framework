from django.urls import path
from Frontend.views import (
    Index, 
    NewDirector,
    NewMovie
)

app_name = "Frontend"

urlpatterns = [
    path("index", Index.as_view(), name='index'),
    path("", Index.as_view(), name='index'),
    path("add-director", NewDirector.as_view(), name='add-director'),
    path("add-movie", NewMovie.as_view(), name='add-movie')
]
