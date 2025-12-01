from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import RecetteViewset, IngredientViewset, EtapePreparationViewset, NotationViewset,ServeurViewset

router = DefaultRouter()
router.register('recettes', RecetteViewset, basename='recettes')
router.register('ingredients', IngredientViewset, basename='ingredients')
router.register('etapes-de-preparation', EtapePreparationViewset, basename='etapes-de-preparation')
router.register('notations', NotationViewset, basename='notations')
router.register('notations', ServeurViewset, basename='notations')

urlpatterns = [
    path('', include(router.urls)),
]
