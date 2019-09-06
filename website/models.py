from django.db import models

# Create your models here.

class Musica(models.Model):
    Nome_Musica = models.CharField(
        max_length = 255,
        verbose_name ='Nome_Musica'
    )

    Artista = models.CharField(
        max_length = 50,
        verbose_name ='Artista'
        )
         
    Genero = models.CharField(
        max_length = 50,
        verbose_name = 'Genero'
    )

    Link_Musica = models.CharField(
        max_length = 50,
        verbose_name = 'Link_Musica'
    )
    
