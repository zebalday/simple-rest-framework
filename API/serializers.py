from rest_framework import serializers
from Backend.models import Director, Movie


class DirectorSerializer(serializers.Serializer):

    class Meta:

        model = Director
        fields = "__all__"


class MovieSerializer(serializers.Serializer):

    class Meta:

        model = Movie
        fields = "__all__"
