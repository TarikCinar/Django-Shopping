# Generated by Django 2.1.15 on 2020-05-27 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=250, verbose_name='Kategöriler')),
            ],
        ),
        migrations.CreateModel(
            name='Urunler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Ürün adı')),
                ('price', models.FloatField(verbose_name='Fiyat')),
                ('category', models.CharField(max_length=250, verbose_name='Kategori')),
                ('image', models.ImageField(upload_to='image/', verbose_name='Resim')),
                ('explanation', models.TextField(verbose_name='Açıklama')),
            ],
        ),
    ]