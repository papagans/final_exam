from webapp.models import Files

from django import forms


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
