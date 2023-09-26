from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


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


class Comment(models.Model):
    post = models.ForeignKey(
        CardShopItem,
        null=True,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='К лоту',
        blank=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор',
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Введите текст комментария',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации',
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return 'Комментарий'
