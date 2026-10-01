from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count

from .models import Autor, Categoria, Livro, Emprestimo
from .serializers import (
    AutorSerializer, CategoriaSerializer, 
    LivroSerializer, EmprestimoSerializer
)

class AutorViewSet(viewsets.ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    @action(detail=False, methods=['get'])
    def com_total_livros(self, request):
        # Usamos annotate() e Count() para contar os livros de cada autor usando o related_name 'livros_escritos'
        autores = Autor.objects.annotate(total_livros=Count('livros_escritos'))
        
        dados = [
            {
                'id': autor.id,
                'nome': autor.nome,
                'total_livros': autor.total_livros
            }
            for autor in autores
        ]
        return Response(dados)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class LivroViewSet(viewsets.ModelViewSet):
    """
    CRUD completo de Livros.
    Inclui uso do Manager Customizado.
    """
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    # ENDPOINT USANDO MANAGER CUSTOMIZADO:
    # Acessível via GET em /api/livros/disponiveis/
    @action(detail=False, methods=['get'])
    def disponiveis(self, request):
        # Chama o método .disponiveis() do nosso LivroManager
        livros = Livro.objects.disponiveis()
        serializer = self.get_serializer(livros, many=True)
        return Response(serializer.data)

class EmprestimoViewSet(viewsets.ModelViewSet):
    """
    CRUD de Empréstimos.
    ENDPOINT PROTEGIDO POR PERMISSÃO: Apenas usuários autenticados podem acessar.
    """
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    permission_classes = [permissions.IsAuthenticated]  # Exige Token JWT