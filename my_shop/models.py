from django.db import models
from django.urls import reverse


# Create your models here.
class Product(models.Model):
    """
    Класс-описание товаров
    """
    name = models.CharField(max_length=150, db_index=True)
    slug = models.CharField(max_length=150, db_index=True, unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)
    description = models.TextField(max_length=1000, blank=True)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    uploaded = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', )
        verbose_name = 'Товар',
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'), )

    def __str__(self):
        return self.name

    def get_display_price(self):
        return '{0:.2f}'.format(self.price / 100)

    def get_absolute_url(self):
        return reverse('my_shop:detail', args=[self.id])