from .models import Estoque, Item
from rest_framework import serializers

class EstoqueSerializer(serializers.ModelSerializer):
    class Meta:
        model= Estoque
        fields = [
            'uuid',
            'name',
            'create_on',
            'minimum'
        ]

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Item
        fields='__all__'