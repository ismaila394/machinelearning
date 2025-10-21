from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField(default="")  # valeur par défaut vide
    moyenne = models.FloatField(default=0)  # valeur par défaut
