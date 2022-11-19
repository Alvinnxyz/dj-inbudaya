from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.

class ProvinceView(generics.ListAPIView):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class BeritaKebudayaanView(generics.ListAPIView):
    queryset = BeritaKebudayaan.objects.all()
    serializer_class = BeritaKebudayaanSerializer
    
class DisekitarAndaView(generics.ListAPIView):
    queryset = DisekitarAnda.objects.all()
    serializer_class = DisekitarAndaSerializer
    
class EventMendatangView(generics.ListAPIView):
    queryset = EventMendatang.objects.all()
    serializer_class = EventMendatangSerializer
    
    
class HomeScreenView(generics.ListAPIView):
    permission_classes = []
    
    def get (self, request, *args, **kwargs):
        berita = BeritaKebudayaan.objects.last()
        disekitar = DisekitarAnda.objects.last()
        event = EventMendatang.objects.last()
        
        data = {
            'berita': BeritaKebudayaanSerializer(berita, many=False).data,
            'disekitar': DisekitarAndaSerializer(disekitar, many=False).data,
            'event': EventMendatangSerializer(event, many=False).data,
        }
        
        return Response(data, status=200)
    
class HomeCategoryView(generics.ListAPIView):
    permission_classes = []
    queryset = Category.objects.all()
    def get (self, request, *args, **kwargs):
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        
        return Response(serializers.data, status=200)