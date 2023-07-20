from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

app_name = 'posts'


def index(request):
    return render(request, 'shop_start/base.html')
