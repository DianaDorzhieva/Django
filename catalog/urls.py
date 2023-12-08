from django.urls import path, include
from catalog.views import contact, home_page

urlpatterns = [
    path('', contact),
    path('', home_page)
]
