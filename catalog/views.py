from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import Http404
from django.shortcuts import render
from catalog.models import Product, Version
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, \
    TemplateView
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from catalog.forms import ProductForm, VersionForm
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here
@login_required
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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:catalog_product')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.name)
            new_mat.save()
        return super().form_valid(form)


class ProductListView(LoginRequiredMixin, ListView):
    model = Product

    def get_queryset(self):
        product_list = super().get_queryset()
        if self.request.user.groups.filter(
            name='Модератор').exists() or self.request.user.is_superuser:
            return product_list
        else:
            return product_list.filter(is_published=True)

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        for object in context['product_list']:

            active_version = Version.objects.filter(product=object, active_version=True).last()
            if active_version:
                object.active_version_number = active_version.number
                object.name_version = active_version.name_version
            else:
                object.active_version_number = None
        return context


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = [
        'catalog.can_change_is_published_permission',
        'catalog.can_change_desc_permission',
        'catalog.can_change_category_permission',
    ]
    success_url = reverse_lazy('catalog:catalog_product')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, extra=1, form=VersionForm)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)

        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

    def get_object(self, queryset=None):

        self.object = super().get_object(queryset)
        if self.request.user.groups.filter(
            name='Модератор').exists() or self.request.user.is_superuser:
            return self.object
        if self.object.author != self.request.user:
            raise Http404("Вы не являетесь владельцем этого товара")
        return self.object


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:catalog_product')

    def get_object(self, queryset=None):

        self.object = super().get_object(queryset)
        if self.request.user.is_superuser:
            return self.object
        if self.object.author != self.request.user:
            raise Http404("Вы не являетесь владельцем этого товара")
        return self.object


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/home_page.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


class ContactView(LoginRequiredMixin, TemplateView):
    template_name = 'catalog/contact.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        return context_data


def toggle_activity(request, pk):
    version_item = get_object_or_404(Version, pk)
    if version_item.active_version:
        version_item.active_version = False
    else:
        version_item.active_version = True

    version_item.save()

    return redirect(reverse('catalog:catalog_product'))


class VersionListView(LoginRequiredMixin, ListView):
    model = Version


class VersionDetailView(LoginRequiredMixin, DetailView):
    model = Version
