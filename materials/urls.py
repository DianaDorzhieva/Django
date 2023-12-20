from django.urls import path, include
from materials.apps import MaterialsConfig

app_name = MaterialsConfig.name
from materials.views import MaterialCreateView

urlpatterns = [
    path('create/', MaterialCreateView.as_view(), name='create'),
    # path('', ..., name='list'),
    # path('edit/<int:pk>', ..., name='edit'),
    # path('view/<int:pk>', ..., name='view'),
    # path('delete/<int:pk>', ..., name='delete')

]
