from django.views.generic import CreateView, ListView, UpdateView,DetailView, DeleteView
from materials.models import Materials
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
class MaterialCreateView(CreateView):
    model = Materials
    fields = ('title', 'body')
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)

class MaterialListView(ListView):
    model = Materials

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset

class MaterialUpdateView(UpdateView):
    model = Materials
    fields = ('title', 'body', 'date_creation', 'is_published')
    #success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('materials:view', args=[self.kwargs.get('pk')])




class MaterialDetailView(DetailView):
    model = Materials

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.title)
            new_mat.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        self.object.save()
        return self.object

class MaterialDeleteView(DeleteView):
    model = Materials
    success_url = reverse_lazy('materials:list')
