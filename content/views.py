from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
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