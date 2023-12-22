from django.urls import path
from catalog.views import contact,  ProductCreateView, ProductDetailView, \
    ProductListView, ProductUpdateView, ProductDeleteView, HomeView, ContactView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('contacts/', contact, name='contacts'),
    path('home/', HomeView.as_view(), name='home'),
    path('catalog_product/', ProductListView.as_view(), name='catalog_product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('view/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('edit/<int:pk>/', ProductUpdateView.as_view(), name='edit_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product')
]
