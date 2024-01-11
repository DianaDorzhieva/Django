from django import forms
from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
                 'полиция', 'радар')
        for word in words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Недопустимое имя продукта - {word}')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман',
                 'полиция', 'радар')
        for word in words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Недопустимое описание продукта - {word}')
        return cleaned_data



class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'



    def clean_active_version(self):
        cleaned_data = self.cleaned_data.get('active_version')
        if cleaned_data:
            version = self.cleaned_data['product'].version_set.filter(active_version=True)
            if version:
                raise forms.ValidationError('Ошибка, у продукта уже есть активная версия!')

        return cleaned_data


