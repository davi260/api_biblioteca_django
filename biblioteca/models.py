from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#Manager Customizado
class LivroManager(models.Manager):
    def disponiveis(self):
       """
       Chamar livros disponiveis
       """ 
       return self.filter(is_disponivel=True)

class PerfilLeitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    telefone = models.CharField(max_length=20, blank=True)
    endereco = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return f"Perfil {self.user.username}"

class Autor(models.Model):
    nome= models.CharField(max_length=100)
    biografia = models.TextField(blank=True)
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome= models.CharField(max_length=50, unique=True)
    def __str__(self):
            return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)

    autor  = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='livros_escritos'
    )

    categorias = models.ManyToManyField(Categoria, related_name='livros')

    is_disponivel = models.BooleanField(default=True)
    ano_publicacao= models.IntegerField(null=True, blank=True)

    objects=LivroManager()

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    leitor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='emprestimos')
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, related_name='emprestimos')
    data_emprestimo = models.DateTimeField(auto_now_add=True)
    data_devolucao = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.livro.titulo} -> {self.leitor.username}"

@receiver(post_save, sender=Emprestimo)
def atualizar_disponibilidade_livro(sender, instance, created, **kwargs):
    """
    - instance: o objeto Emprestimo que acabou de ser salvo.
    - created: True se for um registro NOVO, False se for uma atualização.
    """
    # Se o empréstimo acabou de ser criado e ainda não foi devolvido:
    if created and instance.data_devolucao is None:
        livro = instance.livro
        livro.is_disponivel = False
        livro.save()