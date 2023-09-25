from django.shortcuts import get_object_or_404, render
from django.views.generic.base import TemplateView

from .models import CardShopItem

app_name = 'posts'


class AboutAuthorView(TemplateView):
    template_name = 'about/author.html'


def index(request):
    lot = CardShopItem.objects.all()
    context = {
        'page_obj': lot
    }
    return render(request, 'index.html', context)


def cloth_iews(request, slug):
    group = get_object_or_404(Group, slug=slug)
    lot = group.shop_card.select_related(
        'group'
    )
    context = {
        'page_obj': lot
    }
    return render(request, 'shop_start/в', context)


def shop_iews(request):
    shop = Group.objects.all()
    context = {
        'page_obj': shop
    }
    return render(request, 'shop_start/shop_group.html', context)