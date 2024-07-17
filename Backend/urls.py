from django.urls import path
from Backend.views import NewDirector

app_name = "Backend"

urlpatterns = [
    path("", NewDirector.as_view(), name="add-director")
]
