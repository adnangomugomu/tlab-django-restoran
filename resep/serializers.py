from rest_framework import serializers
from .models import Resep
from bahan.models import Bahan
from kategori.serializers import KategoriSerializers
from bahan.serializers import BahanSerializers

class ResepSerializers(serializers.ModelSerializer):
    bahan = BahanSerializers(many=True, read_only=True, source='bahan_set')
    class Meta:
        model=Resep
        fields='__all__'

    def to_representation(self, instance):
        self.fields['kategori'] =  KategoriSerializers(read_only=True)
        return super(ResepSerializers, self).to_representation(instance)