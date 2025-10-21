from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import NotesViewSet, register_user

router = DefaultRouter()
router.register(r'notes', NotesViewSet, basename='notes')  # ⬅️ AJOUTER basename

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/register/', register_user, name='register'),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]