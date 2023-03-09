# Generated by Django 4.1.7 on 2023-03-06 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_priceservices_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100, unique=True)),
                ('position', models.PositiveSmallIntegerField()),
                ('answer', models.TextField(max_length=300)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]