from django.urls import path
from .views import HomeScreenView, HomeCategoryView

urlpatterns = [
    path('home', HomeScreenView.as_view()),
    path('category', HomeCategoryView.as_view()),
    # path('category/<str:cat>', ),
]

"""
1. Main Screen 
    - Berita Kebudayaan
    - Disekitar Anda
    - Event Mendatang
2. Kategori Budaya
    - All


-- Menampilkan Berita Kebudayaan, Disekitar Anda, Event Mendatang (order by first)
-- Menampilkan Gambar Semua dan Nama Kategori Budaya
"""