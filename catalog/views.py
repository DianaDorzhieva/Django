from django.shortcuts import render
from catalog.models import Product


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
