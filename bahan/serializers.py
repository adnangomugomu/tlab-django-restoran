from rest_framework import serializers
from .models import Bahan

class BahanSerializers(serializers.ModelSerializer):

    class Meta:
        model=Bahan
        fields='__all__'