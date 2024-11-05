from django.db import models
from django.utils import timezone

class Categorias(models.Model):
    """
    Modelo para armazenar Categorias de receitas e despesas, como "Alimentação"
    "Salário", "Transporte" e etc.
    """
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nome
    
    # o __str__ permite retornar um string, neste caso, o nome da categoria
    class Meta:
        verbose_name = "Categorias" # Nome singular para o painel admin
        verbose_name_plural = "Categorias" # nome plural para o painel admin

class Transacao(models.Model):
    TIPOS_TRANSACAO = [
    ('entrada',  'Entrada'), # Para Receitas
    ('saida', 'Saída') # Para Despesas
    ]
    tipo = models.CharField(max_length=7, choices=TIPOS_TRANSACAO)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)
    descricao = models.TextField(blank=True, null=True)
    data = models.DateTimeField(default=timezone.now)
    saldo_total =  models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.valor} on {self.data.strftime('%Y-%m-%d %H:%M:%S')}"
            
    class Meta:
        verbose_name = "Transação"
        verbose_name_plural = "Transações"  