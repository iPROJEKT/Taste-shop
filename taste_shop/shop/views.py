from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings

from .models import CardShopItem, Comment


def page_breakdown(page_number, objects):
    paginator = Paginator(objects, settings.COUNT_POST)
    return paginator.get_page(page_number)


def index(request):
    lot = CardShopItem.objects.all()
    coments = Comment.objects.select_related(
        'post'
    ).count()
    context = {
        'page_obj': lot,
        'comment_count': coments,
        'title': 'Stonks'
    }
    return render(request, 'shop/index.html', context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'shop/contact.html', context)


def product(request):
    lot = CardShopItem.objects.all()
    coments = Comment.objects.select_related(
        'post'
    ).count()
    page_number = request.GET.get('page')
    context = {
        'page_obj': page_breakdown(page_number, lot),
        'comment_count': coments,
        'title': 'Контакты'
    }
    return render(request, 'shop/products.html', context)


def item(request, lot_id):
    lot = get_object_or_404(Comment, id=lot_id)
    context = {
        'lot': lot,
    }
    return render(request, 'shop/item.html', context)


def author(request):
    context = {
        'title': 'Автор сего чуда'
    }
    return render(request, 'shop/about.html', context)
