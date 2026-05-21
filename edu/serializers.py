from rest_framework import serializers
from .models import Autor, Editora

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['id', 'nome']
        read_only_fields = ['id']
    def validate_nome(self, value):
        if Autor.objects.filter(nome=value).exists():
            raise serializers.ValidationError("Autor com esse nome já existe.")
        return value
    
class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = ['id', 'nome']
        read_only_fields = ['id']
    def validate_nome(self, value):
        if Editora.objects.filter(nome=value).exists():
            raise serializers.ValidationError("Editora com esse nome já existe.")
        return value
    