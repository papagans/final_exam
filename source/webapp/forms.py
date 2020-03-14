from webapp.models import Files
from django.core.exceptions import ValidationError

from django import forms


class FileCreationForm(forms.ModelForm):
    title= forms.CharField(required=True, max_length=50, label='Подпись')
    file = forms.FileField(required=True, label='Файл')

    class Meta:
        model = Files
        exclude = ['created_at', 'author','counter']