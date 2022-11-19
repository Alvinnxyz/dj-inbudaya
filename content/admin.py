from django.contrib import admin
from .models import Province, Category, BeritaKebudayaan, DisekitarAnda, EventMendatang
# Register your models here.
admin.site.register([Province, Category, BeritaKebudayaan, DisekitarAnda, EventMendatang])
