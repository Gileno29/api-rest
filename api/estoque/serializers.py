from .models import Estoque
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