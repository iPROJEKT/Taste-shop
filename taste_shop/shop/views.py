from django.shortcuts import render

from .models import CardShopItem

app_name = 'posts'


def index(request):
    lot = CardShopItem.objects.all()
    context = {
        'page_obj': lot
    }
    return render(request, 'shop_start/index.html', context)
