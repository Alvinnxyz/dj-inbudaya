from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
class HomeScreenView(generics.GenericAPIView):
    permission_classes = []
    
    def get (self, request, *args, **kwargs):
        berita = BeritaKebudayaan.objects.last()
        disekitar = DisekitarAnda.objects.last()
        event = EventMendatang.objects.last()
        
        
        data =[HomeBeritaRevision(berita, many=False).data,
               HomeDisekitarRevision(disekitar, many=False).data,
               HomeEventRevision(event, many=False).data,
            ]
        return Response({"home" : data}, status=200)
    
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

class BudayaView(generics.ListAPIView):
    permission_classes = []
    queryset = Category.objects.all()
    def get (self, request, *args, **kwargs):
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        
        return Response(serializers.data, status=200)
       
class IsiBudayaView(generics.ListAPIView):
    permission_classes = []
    queryset = IsiBudaya.objects.all()
    def get (self, request, *args, **kwargs):
        category = IsiBudaya.objects.all()
        serializers = IsiBudayaSerializer(category, many=True)
        
        return Response(serializers.data, status=200)

class ListProvView(generics.ListAPIView):
    permission_classes = []
    serializer_class = ListProvSerializer
    queryset = Category.objects.all()
class ListBudayaView(generics.GenericAPIView):
    permission_classes = []

    def get(self, request, pv, cat):
        pv_id = get_object_or_404(Province, slug=pv).id
        queryset = get_object_or_404(Category, province=pv_id, slug=cat)
        serializer = ListBudayaSerializer(queryset, context={'request': request})
        
        return Response(serializer.data, status=200)
class ListBudayaView(generics.GenericAPIView):
    permission_classes = []

    def get(self, request, pv, cat):
        pv_id = get_object_or_404(Province, slug=pv).id
        queryset = get_object_or_404(Category, province=pv_id, slug=cat)
        serializer = ListBudayaSerializer(queryset, context={'request': request})
        
        return Response(serializer.data, status=200)