from rest_framework import serializers
from content.models import Province, Category, BeritaKebudayaan, DisekitarAnda, EventMendatang, IsiBudaya

def build_absolute_uri(path:str):
    return f"http://127.0.0.1:8000{path}"

# class ProvinceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Province
#         fields = '__all__'
#     img_province = serializers.SerializerMethodField()

#     def get_img_category(self,obj):
#         return build_absolute_uri(f"/media/{obj.img_province}")
class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    province = serializers.SerializerMethodField()
    img_category = serializers.SerializerMethodField()

    def get_img_category(self,obj):
        return build_absolute_uri(f"/media/{obj.img_category}")

    def get_province(self, obj):
        return obj.province.name_province
    class Meta:
        model = Category
        fields = ('name_category', 'img_category', 'province', 'slug')

class BeritaKebudayaanSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeritaKebudayaan
        fields = ('name_berita', 'date_berita', 'judul_berita', 'img_berita', 'des_berita')
    img_berita = serializers.SerializerMethodField()

    def get_img_berita(self,obj):
        return build_absolute_uri(f"/media/{obj.img_berita}")    
class DisekitarAndaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisekitarAnda
        fields = '__all__'
    img_disekitar = serializers.SerializerMethodField()

    def get_img_disekitar(self,obj):
        return build_absolute_uri(f"/media/{obj.img_disekitar}")    
class EventMendatangSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventMendatang
        fields = '__all__'
    img_event = serializers.SerializerMethodField()

    def get_img_event(self,obj):
        return build_absolute_uri(f"/media/{obj.img_event}")

class IsiBudayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsiBudaya
        fields = '__all__'
    img_isibudaya = serializers.SerializerMethodField()

    def get_img_isibudaya(self,obj):
        return build_absolute_uri(f"/media/{obj.img_isibudaya}")

class BudayaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name_category', 'province','img_province')

    img_province= serializers.SerializerMethodField()

    def get_img_budaya(self,obj):
        return build_absolute_uri(f"/media/{obj.img_province}")

class ListProvSerializer(serializers.ModelSerializer):
    list_province = serializers.SerializerMethodField()
    
    def get_list_province(self, obj):
        data = Province.objects.all()
        return ProvinceSerializer(data, many=True).data
    class Meta:
        model = Category
        fields = ('name_category', 'list_province')

class ListBudayaSerializer(serializers.ModelSerializer):
    province = serializers.SerializerMethodField()
    # list_budaya = serializers.SerializerMethodField()

    def get_province(self, obj):
        return obj.province.name_province

    # def get_list_budaya(self, obj):
    #     data = IsiBudaya.objects.filter(province=obj.id)
    #     return [
    #         {
    #             "judul" : o.judul,
    #             "img_isibudaya" : o.img_isibudaya
    #         } for o in data
    #     ]
    class Meta:
        model = Category
        fields = ('name_category', 'province')