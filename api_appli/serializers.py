from rest_framework import serializers
from .models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'type', 'codeGenre']


class LivreSerializer(serializers.ModelSerializer):
    genre = GenreSerializer()

    class Meta:
        model = Livre
        fields = ['id', 'titre', 'auteur', ' status_lecture', 'genre', 'note']


class LecteurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecteur
        fields = '__all__'


class BibliothecaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bibliothecaire
        fields = '__all__'


