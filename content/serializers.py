from rest_framework import serializers
from content.models import Province, Category, BeritaKebudayaan, DisekitarAnda, EventMendatang, IsiBudaya

def build_absolute_uri(path:str):
    return f"http://127.0.0.1:8000{path}"

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
class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = IsiBudaya
        fields = ('judul', 'img_isibudaya', 'des_isibudaya')
class ListBudayaSerializer(serializers.ModelSerializer):
    province = serializers.SerializerMethodField()
    # list_budaya = itemSerializer(many=True)
    list_budaya = serializers.SerializerMethodField()

    def get_province(self, obj):
        return obj.province.name_province
    
    def get_list_budaya(self, obj):
        data = IsiBudaya.objects.filter(category=obj)
        return itemSerializer(data, many=True).data
    class Meta:
        model = Category
        fields = ('name_category', 'province', 'list_budaya')
        
        
"""
{
    'img_url': "sdgafjhbasdhjfb",
    "date": "2021-09-09",
    'deskripsi': 'Ini Judul',
    'main_title': 'Ini Judul Utama',
  },
  {
    'img_url': "sdgafjhbasdhjfb",
    "date": "2021-09-09",
    'deskripsi': 'Ini Judul',
    'main_title': 'Ini Judul Utama',
  },
  {
    'img_url': "sdgafjhbasdhjfb",
    "date": "2021-09-09",
    'deskripsi': 'Ini Judul',
    'main_title': 'Ini Judul Utama',
  }
"""
class HomeBeritaRevision(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    deskripsi = serializers.SerializerMethodField()
    main_title = serializers.SerializerMethodField()
    
    def get_img_url(self, obj):
        return build_absolute_uri(f"/media/{obj.img_berita}")
    
    def get_deskripsi(self, obj):
        return obj.des_berita
    
    def get_main_title(self, obj):
        return obj.name_berita
    
    def get_date(self, obj):
        return obj.date_berita.strftime("%d %B %Y, %H:%M")
    class Meta:
        model = BeritaKebudayaan
        fields = ('img_url', 'date', 'deskripsi', 'main_title')
        
class HomeDisekitarRevision(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    deskripsi = serializers.SerializerMethodField()
    main_title = serializers.SerializerMethodField()
    
    def get_img_url(self, obj):
        return build_absolute_uri(f"/media/{obj.img_disekitar}")
    
    def get_deskripsi(self, obj):
        return obj.judul_disekitar
    
    def get_main_title(self, obj):
        return obj.name_disekitar
    
    def get_date(self, obj):
        return obj.date_disekitar.strftime("%d %B %Y, %H:%M")
    class Meta:
        model = DisekitarAnda
        fields = ('img_url', 'date', 'deskripsi', 'main_title')

class HomeEventRevision(serializers.ModelSerializer):
    img_url = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    deskripsi = serializers.SerializerMethodField()
    main_title = serializers.SerializerMethodField()
    
    def get_img_url(self, obj):
        return build_absolute_uri(f"/media/{obj.img_event}")
    
    def get_deskripsi(self, obj):
        return obj.des_event
    
    def get_main_title(self, obj):
        return obj.name_event
    
    def get_date(self, obj):
        return obj.date_event.strftime("%d %B %Y, %H:%M")
    class Meta:
        model = EventMendatang
        fields = ('img_url', 'date', 'deskripsi', 'main_title')