from django.db import models


class Province(models.Model):
    name_province = models.CharField(max_length=100)
    des_bahasa = models.TextField()
    img_bahasa = models.ImageField(upload_to='gambar/',null=True)
    des_agama = models.TextField()
    img_agama = models.ImageField(upload_to='gambar/',null=True)
    des_kesenian = models.TextField()
    img_kesenian = models.ImageField(upload_to='gambar/',null=True)
    des_khas = models.TextField()
    img_khas = models.ImageField(upload_to='gambar/',null=True)
    des_pakaian = models.TextField()
    img_pakaian = models.ImageField(upload_to='gambar/',null=True)
    des_alatmusik = models.TextField()
    img_alatmusik = models.ImageField(upload_to='gambar/',null=True)
    des_pesan = models.TextField()
    
    def __str__(self):
        return self.name_province

class Mainscreen(models.Model):
    name_mainscreen = models.CharField(max_length=100)
    des_mainscreen = models.TextField()
    img_mainscreen = models.ImageField(upload_to='gambarms/',null=True)
    def __str__(self):
        return self.name_mainscreen

class Kategori(models.Model):
    name_kategori = models.CharField(max_length=100)
    des_kategori = models.TextField()
    img_kategori = models.ImageField(upload_to='gambarkt/',null=True)
    def __str__(self):
        return self.name_kategori

# Create your models here.
