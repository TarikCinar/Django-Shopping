from django.db import models
from urunler.models import Urunler

class Sepet(models.Model):
    product=models.ForeignKey(Urunler,on_delete=models.CASCADE,verbose_name="Ürünler")

class Filtrele(models.Model):
    filtreleme_turu=models.CharField(max_length=250,verbose_name="Filtreleme türü")

class Siparislerim(models.Model):
    siparislerim=models.ForeignKey(Urunler,on_delete=models.CASCADE,verbose_name="Siparislerim")
    date=models.DateTimeField(auto_now=True)
