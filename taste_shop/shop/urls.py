from django.urls import path

from .views import cloth_iews, shop_iews

app_name = 'shop'

urlpatterns = [
    path('', shop_iews, name='grup_iews'),
    path('<slug:slug>/', cloth_iews, name='cloth_iews'),
]
