from django.shortcuts import render

from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.

# Methode CRUD pour Genre
@api_view(['GET', 'POST'])
def genre_list(request):
    # Si la méthode HTTP est GET, récupérer tous les genres depuis la base de données
    # et les sérialiser pour les renvoyer sous forme de réponse
    if request.method == 'GET':
        genres = Genre.objects.all()  # Récupérer tous les genres depuis la base de données
        serializer = GenreSerializer(genres, many=True)  # Sérialiser les genres récupérés
        return Response(serializer.data)  # Renvoyer les données sérialisées

    # Si la méthode HTTP est POST, cela signifie qu'un nouveau genre doit être créé
    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)  # Sérialiser les données reçues depuis la requête
        if serializer.is_valid():  # Vérifier si les données sont valides

            # Si les données sont valides, enregistrer le nouveau genre dans la base de données
            # et renvoyer les données sérialisées avec le statut HTTP 201 Created
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Si les données ne sont pas valides, renvoyer les erreurs avec le statut HTTP 400 Bad Request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def genre_detail(request, pk):
    try:
        genre = Genre.objects.get(pk=pk)
    except Genre.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Methode CRUD pour Livre
class LivreList(APIView):
    """
        List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):  # Affiche livre
        livres = Livre.objects.all()
        serializer = LivreSerializer(livres, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):  # Créer livre
        serializer = LivreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LivreDetail(APIView):
    """
       Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Livre.objects.get(pk)
        except Livre.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        livre = self.get_object(pk)
        serializer = LivreSerializer(livre)
        return Response(serializer.data)

    def put(self, request, pk, format=None):  # MAJ de livre
        livre = self.get_object(pk)
        serializer = LivreSerializer(livre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):  # Supprime livre
        livre = self.get_object(pk)
        livre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        try:
            instance = Livre.objects.get(pk=pk)
        except Livre.DoesNotExist:
            return Response({"error": "Ressource non trouvée"}, status=status.HTTP_404_NOT_FOUND)

        serializer = LivreSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# Méthode CRUD pour Lecteur
class LecteurList(APIView):
    """
        List all lecteurs, or create a new lecteur.
    """
    def get(self, request, format=None):  # Affiche lecteurs
        lecteurs = Lecteur.objects.all()
        serializer = LecteurSerializer(lecteurs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):  # Crée lecteur
        serializer = LecteurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LecteurDetail(APIView):
    """
       Retrieve, update or delete a lecteur instance.
    """
    def get_object(self, pk):
        try:
            return Lecteur.objects.get(pk=pk)
        except Lecteur.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        lecteur = self.get_object(pk)
        serializer = LecteurSerializer(lecteur)
        return Response(serializer.data)

    def put(self, request, pk, format=None):  # MAJ de lecteur
        lecteur = self.get_object(pk)
        serializer = LecteurSerializer(lecteur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):  # Supprime lecteur
        lecteur = self.get_object(pk)
        lecteur.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        lecteur = self.get_object(pk)
        serializer = LecteurSerializer(lecteur, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Méthode CRUD pour bibliothécaire
class BibliothecaireList(APIView):
    """
        List all bibliothécaires, or create a new bibliothécaire.
    """
    def get(self, request, format=None):  # Affiche bibliothécaires
        bibliothecaires = Bibliothecaire.objects.all()
        serializer = BibliothecaireSerializer(bibliothecaires, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):  # Crée bibliothécaire
        serializer = BibliothecaireSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BibliothecaireDetail(APIView):
    """
       Retrieve, update or delete a bibliothécaire instance.
    """
    def get_object(self, pk):
        try:
            return Bibliothecaire.objects.get(pk=pk)
        except Bibliothecaire.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bibliothecaire = self.get_object(pk)
        serializer = BibliothecaireSerializer(bibliothecaire)
        return Response(serializer.data)

    def put(self, request, pk, format=None):  # MAJ de bibliothécaire
        bibliothecaire = self.get_object(pk)
        serializer = BibliothecaireSerializer(bibliothecaire, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):  # Supprime bibliothécaire
        bibliothecaire = self.get_object(pk)
        bibliothecaire.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        bibliothecaire = self.get_object(pk)
        serializer = BibliothecaireSerializer(bibliothecaire, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)