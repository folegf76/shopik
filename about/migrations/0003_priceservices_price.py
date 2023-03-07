# Generated by Django 4.1.7 on 2023-03-06 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_imgservices_ourservices_priceservices'),
    ]

    operations = [
        migrations.AddField(
            model_name='priceservices',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
            preserve_default=False,
        ),
    ]
