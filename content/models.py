from django.db import models

class Province(models.Model):
    name_province = models.CharField(max_length=100)
    img_province = models.ImageField(upload_to='gambar/',null=True, blank=True)
    slug = models.CharField(max_length=10, null=True)
    def serialize(self):
        return ({
            "img_province": self.img_province.url
        })
    def __str__(self):
        return self.name_province
class Category(models.Model):
    name_category = models.CharField(max_length=100)
    img_category = models.ImageField(upload_to='gambar/',null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, null=True)
    slug = models.CharField(max_length=10, null=True)

    #provinsi = models.ManyToManyField(Province)
    def serialize(self):
        return {
            "img_category": self.img_category.url
        }
    def __str__(self):
        return self.name_category

class IsiBudaya(models.Model):
    judul = models.CharField(max_length=100)
    img_isibudaya = models.ImageField(upload_to='gambar/',null=True, blank=True)
    des_isibudaya = models.TextField()
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.judul

    
class BeritaKebudayaan(models.Model):
    judul_berita = models.CharField(max_length=100, null=True, blank=True)
    name_berita = models.CharField(max_length=100)
    des_berita = models.TextField()
    date_berita = models.DateField()
    img_berita = models.ImageField(upload_to='gambar/',null=True, blank=True)
    def serialize(self):
        return ({
            "img_berita": self.img_berita.url
        })
    def __str__(self):
        return self.name_berita
class DisekitarAnda(models.Model):
    judul_disekitar = models.CharField(max_length=100, null=True, blank=True)
    name_disekitar = models.CharField(max_length=100)
    des_disekitar = models.TextField()
    date_disekitar = models.DateField()
    img_disekitar = models.ImageField(upload_to='gambar/',null=True, blank=True)
    def serialize(self):
        return ({
            "img_disekitar": self.img_disekitar.url
        })
    def __str__(self):
        return self.name_disekitar
    
class EventMendatang(models.Model):
    judul_event = models.CharField(max_length=100, null=True, blank=True)
    name_event = models.CharField(max_length=100)
    des_event = models.TextField()
    date_event = models.DateField()
    img_event = models.ImageField(upload_to='gambar/',null=True, blank=True)
    
    def serialize(self):
        return ({
            "img_event": self.img_event.url
        })
    def __str__(self):
        return self.name_event
    
