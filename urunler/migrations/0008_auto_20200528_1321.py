# Generated by Django 2.1.15 on 2020-05-28 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0007_urunler_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urunler',
            name='upload_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Eklenme tarihi'),
        ),
    ]
