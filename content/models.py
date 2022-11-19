from django.db import models

class Province(models.Model):
    name_province = models.CharField(max_length=100)
    pesan = models.TextField()
    
    def __str__(self):
        return self.name_province
class Category(models.Model):
    name_category = models.CharField(max_length=100)
    des_category = models.TextField()
    img_category = models.ImageField(upload_to='gambar/',null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name_category
    
    
class BeritaKebudayaan(models.Model):
    name_berita = models.CharField(max_length=100)
    des_berita = models.TextField()
    date_berita = models.DateField()
    img_berita = models.ImageField(upload_to='gambar/',null=True, blank=True)
    
    def __str__(self):
        return self.name_berita
class DisekitarAnda(models.Model):
    name_disekitar = models.CharField(max_length=100)
    des_disekitar = models.TextField()
    date_disekitar = models.DateField()
    img_disekitar = models.ImageField(upload_to='gambar/',null=True, blank=True)
    
    def __str__(self):
        return self.name_disekitar
    
class EventMendatang(models.Model):
    name_event = models.CharField(max_length=100)
    des_event = models.TextField()
    date_event = models.DateField()
    img_event = models.ImageField(upload_to='gambar/',null=True, blank=True)
    
    def __str__(self):
        return self.name_event
        