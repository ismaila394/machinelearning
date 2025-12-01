from rest_framework import serializers
from .models import Recette, Ingredient, EtapePreparation, Notation

class RecetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recette
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class EtapePreparationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EtapePreparation
        fields = '__all__'

class NotationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notation
        fields = '__all__'
