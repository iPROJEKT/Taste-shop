from django.shortcuts import render
from django.core.paginator import Paginator
from django.conf import settings

from .models import CardShopItem, Comment


def page_breakdown(page_number, objects):
    paginator = Paginator(objects, settings.COUNT_POST)
    return paginator.get_page(page_number)


def author(request):
    context = {
        'title': 'Автор сего чуда'
    }
    return render(request, 'about.html', context)


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
    return render(request, 'index.html', context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'contact.html', context)


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
    return render(request, 'products.html', context)