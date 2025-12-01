from django.db import models
from django.contrib.auth.models import User

class Recette(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    duree = models.IntegerField()  # Duration in minutes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50)
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE, related_name="ingredients")

    def __str__(self):
        return self.name

class EtapePreparation(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE, related_name="etapes")
    etape_numero = models.IntegerField()
    instruction = models.TextField()

    def __str__(self):
        return f"Etape {self.etape_numero} pour {self.recette.title}"

class Notation(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE, related_name="notations")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()  
    commentaire = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notation de {self.user.username} pour {self.recette.title}: {self.score}"
    
class Serveur(models.Model):
    name= models.TextField(blank=True, null=True)
    age=models.IntegerField()
    localite=models.CharField(max_length=100)


    def __str__(self):
        return self.name
