from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter
from .models import Musica
from .serializers import MusicaSerializer

class MusicaViewSet(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^Nome_Musica','=Artista','=Genero','=Link_Musica']
    queryset = Musica.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
    serializer_class = MusicaSerializer