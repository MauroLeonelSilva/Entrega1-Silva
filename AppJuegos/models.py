from django.db import models

# Create your models here.



class VideoJuegoModel(models.Model):
    nombre=models.CharField(max_length=50)
    calificacion=models.IntegerField()
    genero=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre+" "+str(self.calificacion)+" "+self.genero

class carta(models.Model):
    Nombrejuego=models.CharField(max_length=50)
    Nombrecarta=models.CharField(max_length=50)
    Rareza=models.CharField(max_length=10)

    def __str__(self):
        return self.Nombrejuego+" "+self.Nombrecarta+" "+self.Rareza

class juegosdecartas(models.Model):
    Nombrejuego= models.CharField(max_length=50)
    Nombrecarta= models.CharField(max_length=50)
    Rareza= models.CharField(max_length=50)
    

    def __str__(self):
        return self.Nombrejuego+" "+self.Nombrecarta+" "+self.Rareza

class juegosdemesaModel(models.Model):
    Nombrejuego= models.CharField(max_length=50)
    Tipo_juego= models.CharField(max_length=50)
    Cantidad_jugadores= models.IntegerField()
    

    def __str__(self):
        return self.Nombrejuego+" "+self.Tipo_juego+" "+str(self.Cantidad_jugadores)