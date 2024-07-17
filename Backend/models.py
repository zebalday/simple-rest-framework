from django.db import models


class Director(models.Model):


    name = models.CharField(max_length=100, null=False, blank=False)
    birthday = models.DateField(null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self) -> str:
        
        return (f"{self.name}, {self.country}")



class Movie(models.Model):


    name = models.CharField(max_length=120, null=False, blank=False)
    release_date = models.DateField(null=False, blank=False)
    category = models.CharField(max_length=100, null=False, blank=False)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=False, blank=False)
    description = models.TextField(max_length=500,null=False, blank=False)

    def __str__(self) -> str:

        return (f"{self.name}, {self.director.name}")


