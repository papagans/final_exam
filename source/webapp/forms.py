from webapp.models import Files
from django.core.exceptions import ValidationError

from django import forms


# class FileCreationForm(forms.ModelForm):
#     title= forms.CharField(required=True, max_length=50, label='Подпись')
#     file = forms.FileField(required=True, label='Файл')
#
#     class Meta:
#         model = Files
#         exclude = ['created_at', 'author','counter']


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Найти')


class AnonymCreationForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['title', 'file']


class FileCreationForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['file', 'title', 'access']
