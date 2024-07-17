from django.urls import path
from API.views import DirectorApiView, MovieApiView

app_name = "API"

urlpatterns = [
    path("directors", DirectorApiView.as_view(), name='director-api-list'),
    path("movies", MovieApiView.as_view(), name='movie-api-list')
]
