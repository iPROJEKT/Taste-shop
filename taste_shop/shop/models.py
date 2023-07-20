from django.db import models
from colorfield.fields import ColorField

from .validator import is_valid_hexa_code


class Tag(models.Model):
    name = models.CharField(
        unique=True,
        max_length=100,
    )
    color = ColorField(
        validators=[is_valid_hexa_code],
        unique=True,
    )
    slug = models.SlugField(
        unique=True,
        max_length=30
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Тэги'


class Group(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=200)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='URL',
    )
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазины'


class CardShopItem(models.Model):
    SIZE = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )
    name = models.CharField(
        max_length=100
    )
    size = models.CharField(
        choices=SIZE,
        max_length=100
    )
    description = models.TextField(
        blank=False,
        null=False,
    )
    image = models.ImageField(
        upload_to='media/recipes/images/',
        blank=False,
        null=False,
    )
    tags = models.ManyToManyField(
        Tag,
        max_length=100
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='shop_card',
        help_text='Магазин к которому будет относиться этот лот',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Лот'
        verbose_name_plural = 'Одежда'
