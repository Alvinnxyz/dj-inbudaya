from rest_framework import serializers
from content.models import Province, Category, BeritaKebudayaan, DisekitarAnda, EventMendatang



class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    province = serializers.SerializerMethodField()
    
    def get_province(self, obj):
        return obj.province.name_province
    
    class Meta:
        model = Category
        fields = ('name_category', 'img_category', 'province')

class BeritaKebudayaanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeritaKebudayaan
        fields = ('name_berita', 'date_berita', 'judul_berita', 'img_berita', 'des_berita')
        
class DisekitarAndaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisekitarAnda
        fields = '__all__'
        
class EventMendatangSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventMendatang
        fields = '__all__'


