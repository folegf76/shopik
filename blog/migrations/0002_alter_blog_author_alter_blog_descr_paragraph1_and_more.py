# Generated by Django 4.1.7 on 2023-03-05 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='blog',
            name='descr_paragraph1',
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='blog',
            name='descr_paragraph2',
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='blog',
            name='descr_paragraph3',
            field=models.TextField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='blog',
            name='descr_paragraph4',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]
