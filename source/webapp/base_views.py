from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic import ListView as DjangoListView

from webapp.forms import SimpleSearchForm


class SimpleSearchView(DjangoListView):
    search_form_class = SimpleSearchForm
    form_search_field = 'search'

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_query = self.get_search_query()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        if self.search_query:
            data = {self.form_search_field: self.search_query}
            context['query'] = urlencode(data)
        context['form'] = self.form
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_query:
            query = self.get_query()
            queryset = queryset.filter(query).distinct()
        return queryset

    def get_query(self):
        return Q()

    def get_search_form(self):
        return self.search_form_class(self.request.GET)

    def get_search_query(self):
        if self.form.is_valid():
            return self.form.cleaned_data[self.form_search_field]
        return None