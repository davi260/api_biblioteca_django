from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Autor, Categoria, Livro, Emprestimo, PerfilLeitor


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'


class LivroSerializer(serializers.ModelSerializer):
    # Serializer Aninhado (Nested Serializer)
    autor_detalhes = AutorSerializer(source='autor', read_only=True)
    categorias_detalhes = CategoriaSerializer(source='categorias', many=True, read_only=True)

    class Meta:
        model = Livro
        fields = [
            'id', 
            'titulo', 
            'autor',                # ID do autor para cadastrar/editar
            'autor_detalhes',       # Objeto completo do autor na resposta da API
            'categorias',           # Lista de IDs das categorias
            'categorias_detalhes',  # Lista de objetos das categorias na resposta
            'is_disponivel', 
            'ano_publicacao'
        ]


class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']