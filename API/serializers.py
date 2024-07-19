from rest_framework import serializers
from Backend.models import Director, Movie


class DirectorSerializer(serializers.ModelSerializer):

    class Meta:

        model = Director
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):

    class Meta:

        model = Movie
        fields = "__all__"
