from django.db import models


class CardShopItem(models.Model):
    SIZE = (
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )
    TAGS = (
        ('Shoes', 'Shoes'),
        ('Socks', 'Socks'),
        ('Underpants', 'Underpants'),
        ('Trousers', 'Trousers'),
        ('Shorts', 'Shorts'),
        ('T-shirt', 'T-shirt'),
        ('Hoodie', 'Hoodie'),
        ('Jacket', 'Jacket'),
        ('Sweater', 'Sweater'),
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
        upload_to='shouse/',
        blank=False,
        null=False,
    )
    tag = models.CharField(
        choices=TAGS,
        max_length=100,
    )
    slug = models.SlugField(
        max_length=255,
        unique=True,
        verbose_name='URL',
    )
    prise = models.IntegerField(
        blank=False,
        null=False,
        default=0
    )
    amount = models.IntegerField(
        blank=False,
        null=False,
        default=0
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Лот'
        verbose_name_plural = 'Одежда'
