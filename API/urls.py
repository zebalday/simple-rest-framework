from django.urls import path, include
from rest_framework.routers import DefaultRouter
from API.views import (
    DirectorApiView, 
    MovieApiView, 
    DirectorViewSets, 
    MovieViewSets
    )


app_name = "API"

router = DefaultRouter()
router.register(r"directors", DirectorViewSets, 'director',)
router.register(r"movies", MovieViewSets, 'movie')


urlpatterns = [
    path("directors", DirectorApiView.as_view(), name='director-apiview'),
    path("movies", MovieApiView.as_view(), name='movie-apiview'),
    path('viewsets/', include((router.urls, 'viewsets')))
]
