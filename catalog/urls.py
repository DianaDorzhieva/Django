from django.urls import path, include
from catalog.views import contact, home_page, product
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contact, name='contacts'),
    path('home/', home_page, name='home'),
    path('catalog_product/', product, name='catalog_product')
]
