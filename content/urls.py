from django.urls import path
from .views import BeritaView, HomeScreenView, HomeCategoryView, BudayaView, IsiBudayaView,ListBudayaView,ListProvView

urlpatterns = [
    path('home', HomeScreenView.as_view()),
    path('category', HomeCategoryView.as_view()),
    path('berita/<pk>', BeritaView.as_view()),
    path('budaya', BudayaView.as_view()),
    path('isi_budaya', IsiBudayaView.as_view()),
    path('listbudaya/<str:pv>/<str:cat>', ListBudayaView.as_view()),
    path('listprov', ListProvView.as_view())
    # path('category/<str:cat>', ),
]

"""
1. Main Screen 
    - Berita Kebudayaan
    - Disekitar Anda
    - Event Mendatang
2. Kategori Budaya
    - All
#fdd835]

-- Menampilkan Berita Kebudayaan, Disekitar Anda, Event Mendatang (order by first)
-- Menampilkan Gambar Semua dan Nama Kategori Budaya
-- Menampilkan Judul, Tanggal, Deskripsi, Gambar Berita Kebudayaan dan List Berita Kebudayaan lainnya
"""