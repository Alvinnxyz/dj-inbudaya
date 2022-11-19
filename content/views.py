from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import *
from .serializers import *

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
    
class BeritaView(generics.GenericAPIView, mixins.RetrieveModelMixin):
    queryset = BeritaKebudayaan.objects.all()
    serializer_class = BeritaKebudayaanSerializer
    def get(self, request, pk=None):
        if pk:
            data_detail = BeritaKebudayaan.objects.get(id=pk)
            data_semua = self.get_queryset().exclude(id=pk)
            serializers = BeritaKebudayaanSerializer(data_semua, many=True)
            
            return Response({
                "berita" : self.get_serializer(data_detail).data,
                "artikel" : serializers.data
            }, status=200)
            # return self.retrieve(request)
        else:
            # return self.list(request)
            return Response({'message': 'Not found'}, status=404)
        