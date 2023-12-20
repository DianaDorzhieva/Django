from django.views.generic import CreateView, ListView
from materials.models import Materials
from django.urls import reverse_lazy

# class MaterialCreateView(CreateView):
#     model = Materials
#     fields = ('title', 'body')
#     success_url = reverse_lazy('materials:list')
#
# class MaterialListView(ListView):
#     model = Materials

