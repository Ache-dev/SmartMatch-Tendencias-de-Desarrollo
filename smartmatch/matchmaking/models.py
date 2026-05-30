from django.db import models

class Person(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    deporte = models.CharField(max_length=100)
    musica = models.CharField(max_length=100)
    mascota = models.CharField(max_length=100)
    personalidad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class MatchTraining(models.Model):
    edad_diff = models.IntegerField()
    mismo_deporte = models.IntegerField()
    misma_musica = models.IntegerField()
    misma_mascota = models.IntegerField()
    misma_personalidad = models.IntegerField()
    match = models.IntegerField()

    def __str__(self):
        return f"Diff Edad: {self.edad_diff} - Match: {self.match}"