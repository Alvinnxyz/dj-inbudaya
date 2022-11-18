from content.models import Province, Mainscreen, Kategori
from rest_framework import serializers

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

class MainscreenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mainscreen
        fields = '__all__'

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = '__all__'

