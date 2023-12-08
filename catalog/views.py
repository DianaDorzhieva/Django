from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'catalog/contact.html')

def home_page(request):
    return render(request, 'catalog/home_page.html')
