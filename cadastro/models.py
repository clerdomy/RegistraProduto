from django.db import models

class Produto(models.Model):
    """
    Modelo que representa um produto.

    Attributes:
        nome (str): O nome do produto (limite de 120 caracteres).
        valor (Decimal): O valor do produto com até 10 dígitos, incluindo 2 casas decimais.
        disponivel (bool): Indica se o produto está disponível ou não.
        descricao (str): A descrição do produto.

    Methods:
        __str__(): Retorna uma representação de string do produto.
    """

    nome = models.CharField(max_length=120)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)
    descricao = models.TextField()

    def __str__(self):
        """
        Retorna uma representação de string do produto.

        Returns:
            str: Uma representação de string do produto.
        """
        return f"Nome do Produto: {self.nome} | Disponível: {self.get_disponivel_display()} | Preço: {self.valor}"
