# Generated by Django 2.1.15 on 2020-05-27 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('urunler', '0003_auto_20200527_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='AltCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_category_name', models.CharField(max_length=250, verbose_name='Kategöriler')),
            ],
        ),
    ]
