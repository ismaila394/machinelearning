from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mes_notes_privees.urls')),  # Inclure les URLs de votre app
]