
from django.db import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    position = models.PositiveSmallIntegerField()
    image = models.ImageField(upload_to='blogs/%Y/%m/%d', blank=True)
    short_descr = models.TextField(max_length=100)
    descr_paragraph1 = models.TextField(max_length=400, blank=True)
    descr_paragraph2 = models.TextField(max_length=400, blank=True)
    descr_paragraph3 = models.TextField(max_length=400, blank=True)
    descr_paragraph4 = models.TextField(max_length=400, blank=True)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return f'{self.name}  {self.author}'

