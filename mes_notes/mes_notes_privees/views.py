from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import Notes
from .serializers import NotesSerializer

class NotesViewSet(viewsets.ModelViewSet):
    serializer_class = NotesSerializer
    permission_classes = [IsAuthenticated]
    queryset = Notes.objects.all()  # ⬅️ AJOUTER CETTE LIGNE

    def get_queryset(self):
        # Surcharger pour ne retourner que les notes de l'utilisateur connecté
        return Notes.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, moyenne=0)

    # 🔹 Action publique pour voir les notes sans authentification
    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def public_notes(self, request):
        """
        Permet de voir les notes sans authentification avec le nom d'utilisateur
        """
        username = request.query_params.get('username')
        
        if not username:
            return Response(
                {"error": "Le paramètre username est requis"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            user = User.objects.get(username=username)
            notes = Notes.objects.filter(user=user)
            serializer = self.get_serializer(notes, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(
                {"error": "Utilisateur non trouvé"}, 
                status=status.HTTP_404_NOT_FOUND
            )

    # 🔹 Dupliquer une note
    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def duplicate(self, request, pk=None):
        note = self.get_object()
        note.pk = None
        note.moyenne = 0
        note.save()
        serializer = self.get_serializer(note)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 🔹 Vue pour l'inscription des nouveaux utilisateurs
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    """
    Inscription d'un nouvel utilisateur
    """
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email', '')
    
    if not username or not password:
        return Response(
            {"error": "Le nom d'utilisateur et le mot de passe sont requis"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "Ce nom d'utilisateur est déjà pris"}, 
            status=status.HTTP_400_BAD_REQUEST
        )
    
    try:
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        return Response(
            {"message": "Utilisateur créé avec succès", "user_id": user.id}, 
            status=status.HTTP_201_CREATED
        )
    except Exception as e:
        return Response(
            {"error": f"Erreur lors de la création: {str(e)}"}, 
            status=status.HTTP_400_BAD_REQUEST
        )