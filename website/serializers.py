from rest_framework import serializers
from .models import Musica


class MusicaSerializer(serializers.ModelSerializer):
     class Meta:
         model = Musica 
         fields =('Nome_Musica','Artista','Genero','Link_Musica')