from django.urls import path

from .views import cloth_iews, shop_iews, index

app_name = 'shop'

urlpatterns = [

    path('', index, name='grup_iews'),
    path('<slug:slug>/', cloth_iews, name='cloth_iews'),
    path('shop/', shop_iews, name='shop_iews'),
]
