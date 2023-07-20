from django.contrib import admin


from .models import (
    Tag, CardShopItem,
    Group
)

admin.site.register(Tag)
admin.site.register(CardShopItem)
admin.site.register(Group)
