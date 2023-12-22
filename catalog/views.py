from django.shortcuts import render
from catalog.models import Product
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView,TemplateView
from django.urls import reverse_lazy
from pytils.translit import slugify


# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Имя {name}, телефон {phone}, текст {message}')
    return render(request, 'catalog/contact.html')





# def product(request):
#     product_list = Product.objects.all()
#     context = {
#         'object_list': product_list
#     }
#     return render(request, 'catalog/product.html', context)


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price_one', 'date_creation',
              'date_last_modification')
    success_url = reverse_lazy('catalog:catalog_product')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)



class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product

class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price_one', 'date_creation',
              'date_last_modification')
    success_url = reverse_lazy('catalog:catalog_product')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:catalog_product')

class HomeView(TemplateView):
    template_name = 'catalog/home_page.html'
    def get_context_data(self,**kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data

class ContactView(TemplateView):
    template_name = 'catalog/contact.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data
