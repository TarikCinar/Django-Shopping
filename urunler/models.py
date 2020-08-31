from django.db import models

class Category(models.Model):
    category_name=models.CharField(max_length=250,verbose_name="Kategöriler")

    def __str__(self):
        return self.category_name
class AltCategory(models.Model):
    ust_category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Üst kategory")
    alt_category_name=models.CharField(max_length=250,verbose_name="Alt Karegori")

    def __str__(self):
        return self.alt_category_name

class Urunler(models.Model):
    name=models.CharField(max_length=250,verbose_name="Ürün adı")
    price=models.FloatField(verbose_name="Fiyat")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Kategori")
    alt_category=models.ForeignKey(AltCategory,on_delete=models.CASCADE,verbose_name="Kategori")
    image=models.ImageField(upload_to='image/',verbose_name="Resim")
    explanation=models.TextField(verbose_name="Açıklama")
    upload_date=models.DateTimeField(auto_now=True,verbose_name="Eklenme tarihi")
    seller=models.CharField(max_length=250,verbose_name="Satıcı")

    def __str__(self):
        return self.name
