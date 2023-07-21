from django.db import models


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
        upload_to='images/',
        blank=False,
        null=False,
    )
    tag = models.CharField(
        choices=TAGS,
        max_length=100,
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='shop_card',
        help_text='Магазин к которому будет относиться этот лот',
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
