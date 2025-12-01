from django.contrib import admin
from .models import Recette, Ingredient, EtapePreparation, Notation,Serveur

admin.site.register(Recette)
admin.site.register(Ingredient)
admin.site.register(EtapePreparation)
admin.site.register(Notation)
admin.site.register(Serveur)
