from django.urls import path

from .views import cloth_iews, shop_iews, index, AboutAuthorView

app_name = 'shop'

urlpatterns = [

    path('', index, name='grup_iews'),
    path('au/', AboutAuthorView.as_view(), name='author'),
    path('shop/', shop_iews, name='shop_iews'),
    path('shop/<slug:slug>/', cloth_iews, name='cloth_iews'),
]
