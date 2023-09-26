from django.urls import path

from .views import index, author, contact, product

app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    path('autor/', author, name='autor'),
    path('contact/', contact, name='contact'),
    path('product/', product, name='product')
]
