from django.urls import path
from Backend.views import NewDirector, NewMovie

app_name = "Backend"

urlpatterns = [
    path("new-director", NewDirector.as_view(), name="add-director"),
    path("new-movie", NewMovie.as_view(), name="add-movie")
]
