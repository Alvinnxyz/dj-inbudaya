
from django.contrib import admin
from django.urls import path, include

# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('province', ProvinceViewset)
# router.register('mainscreen', MainscreenViewset)
# router.register('kategori', KategoriViewset)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("content.urls")),

]
