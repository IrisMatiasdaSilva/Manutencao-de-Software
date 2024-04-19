from django.db import models

class Produto(models.Model):
    nome_produto = models.CharField(max_length=100)
    preco_por_unidade_produto = models.DecimalField(max_digits=6, decimal_places=2)
    estoque_disponivel = models.IntegerField()
    class Meta:
        abstract = True
    def __str__(self):
        return self.nome_produto
    
class Verduras(Produto):
    class Meta:
        verbose_name_plural = "Verduras"
    
class Frutas(Produto):
    class Meta:
        verbose_name_plural = "Produtos"

class Entrega(models.Model):
    nome_cliente = models.CharField(max_length=255)
    local_de_entrega = models.TextField()
    data_prevista_entrega = models.DateTimeField()
    pagamento = models.OneToOneField('Pagamento', on_delete=models.CASCADE, related_name='entrega')
    def __str__(self):
        return self.nome_cliente

class Pagamento(models.Model):
    forma_de_pagamento = models.CharField(max_length=50)
    valor_geral = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):
        return self.forma_de_pagamento

class Item(models.Model):
    entrega_do_item = models.ForeignKey(Entrega, on_delete=models.CASCADE, related_name="itens")
    nome_item = models.CharField(max_length=100)
    quantidade_item = models.IntegerField()
    preco_unitario_do_item = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return  f"{self.nome_item}"
