# Generated by Django 2.1.15 on 2020-05-28 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filtrele',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filtreleme_turu', models.CharField(max_length=250, verbose_name='Filtreleme türü')),
            ],
        ),
    ]