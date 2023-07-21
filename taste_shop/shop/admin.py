from django.contrib import admin


from .models import (
    CardShopItem,
    Group
)

admin.site.register(CardShopItem)
admin.site.register(Group)
