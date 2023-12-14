from django.urls import path, include
from catalog.views import contact, home_page, product

urlpatterns = [
    path('contacts/', contact),
    path('home/', home_page),
    path('product/', product)
]
