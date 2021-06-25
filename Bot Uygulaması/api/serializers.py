from rest_framework import serializers
from .models import SoruModel, CevapModel, KategoriModel

class CevapSerializer(serializers.ModelSerializer):
    class Meta:
        model = CevapModel
        fields = [
            'id',
            'cevap',
            'dogruMu',
        ]

class rastgeleSoruSerializer(serializers.ModelSerializer):

    cevap = CevapSerializer(many=True, read_only=True)

    class Meta:
        model = SoruModel
        fields = [
            'baslik',
            'cevap'
        ]