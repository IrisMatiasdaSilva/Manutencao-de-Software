from rest_framework import serializers
from app.models import Verduras, Frutas, Entrega, Pagamento, Item

class VerdurasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Verduras
        fields = ['nome_produto', 'preco_por_unidade_produto', 'estoque_disponivel']

class FrutasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Frutas
        fields = ['nome_produto', 'preco_por_unidade_produto', 'estoque_disponivel']

class EntregaSerializer(serializers.ModelSerializer):
    itens = serializers.PrimaryKeyRelatedField(many=True, queryset=Item.objects.all())
    pagamento = serializers.PrimaryKeyRelatedField(queryset=Pagamento.objects.all())

    class Meta:
        model = Entrega
        fields = ['nome_cliente', 'local_de_entrega', 'data_prevista_entrega', 'itens', 'pagamento']

class PagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagamento
        fields = ['forma_de_pagamento', 'valor_geral']

class ItemSerializer(serializers.ModelSerializer):
    entrega_do_item = serializers.PrimaryKeyRelatedField(queryset=Entrega.objects.all())

    class Meta:
        model = Item
        fields = ['nome_item', 'quantidade_item', 'preco_unitario_do_item', 'entrega_do_item']

