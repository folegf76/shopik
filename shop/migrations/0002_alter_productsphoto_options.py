# Generated by Django 4.1.7 on 2023-03-09 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productsphoto',
            options={'ordering': ('id_product',)},
        ),
    ]
