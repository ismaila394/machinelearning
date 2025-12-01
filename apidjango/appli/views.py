from rest_framework.viewsets import ModelViewSet
from .models import Recette, Ingredient, EtapePreparation, Notation
from .serializer import RecetteSerializer, IngredientSerializer, EtapePreparationSerializer, NotationSerializer

class RecetteViewset(ModelViewSet):
    queryset = Recette.objects.all()
    serializer_class = RecetteSerializer

class IngredientViewset(ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

class EtapePreparationViewset(ModelViewSet):
    queryset = EtapePreparation.objects.all()
    serializer_class = EtapePreparationSerializer

class NotationViewset(ModelViewSet):
    queryset = Notation.objects.all()
    serializer_class = NotationSerializer
