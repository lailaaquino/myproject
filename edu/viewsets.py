from rest_framework import viewsets, permissions
from .models import Autor, Editora
from .serializers import AutorSerializer, EditoraSerializer

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EditoraViewSet(viewsets.ModelViewSet):
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]