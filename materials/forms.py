from django import forms
from service.models import Сustomer, Letter, Message


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(max_length=250)


class СustomerForm(forms.ModelForm):
    class Meta:
        model = Сustomer
        fields = '__all__'


class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = '__all__'


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
