
from django.shortcuts import get_object_or_404, render

from .models import Group

app_name = 'posts'


def index(request):
    return render(request, 'shop_start/start_page.html')


def cloth_iews(request, slug):
    group = get_object_or_404(Group, slug=slug)
    lot = group.shop_card.select_related(
        'group'
    )
    context = {
        'page_obj': lot
    }
    return render(request, 'shop_start/index.html', context)


def shop_iews(request):
    shop = Group.objects.all()
    context = {
        'page_obj': shop
    }
    return render(request, 'shop_start/shop_group.html', context)