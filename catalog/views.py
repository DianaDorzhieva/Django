from django.shortcuts import render
from catalog.models import Product
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя {name}, телефон {phone}, текст {message}')
    return render(request, 'catalog/contact.html')


def home_page(request):
    return render(request, 'catalog/home_page.html')


def product(request):
    product_list = Product.objects.all()
    context = {
        'object_list': product_list
    }
    return render(request, 'catalog/product.html', context)


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price_one', 'date_creation',
              'date_last_modification')
    success_url = reverse_lazy('catalog:product_list')

class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price_one', 'date_creation',
              'date_last_modification')
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
