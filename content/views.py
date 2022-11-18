from django.shortcuts import render
from rest_framework import viewsets
from .models import Province
from inbudaya.serializers import *

# Create your views here.
class ProvinceViewset(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class MainscreenViewset(viewsets.ModelViewSet):
    queryset = Mainscreen.objects.all()
    serializer_class = MainscreenSerializer

class KategoriViewset(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer



