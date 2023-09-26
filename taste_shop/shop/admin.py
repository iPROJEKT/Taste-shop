from django.contrib import admin


from .models import (
    CardShopItem,
    Comment
)

admin.site.register(CardShopItem)
admin.site.register(Comment)
