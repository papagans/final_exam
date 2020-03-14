from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import ListView, DetailView, CreateView,\
    UpdateView, DeleteView, FormView, View
# from django.core.paginator import Paginator
#
from webapp.forms import AnonymCreationForm, FileCreationForm, SimpleSearchForm
from .base_views import SimpleSearchView
from webapp.models import Files
# Create your views here.


# class IndexView(ListView):
#     template_name = 'index.html'
#     context_object_name = 'files'
#     model = Files
#     # ordering = ['-created_at']


class IndexView(ListView):
    template_name = 'index.html'
    model = Files
    context_object_name = 'files'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        # context['files'] = Files.objects.all().filter(access='public')
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(title__icontains=self.search_value, access__icontains='public')
            queryset = queryset.filter(query)
            return queryset
        else:
            return queryset.filter(access='public')

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None



class FilesCreateView(CreateView):
    model = Files
    template_name = 'file_create.html'
    # fields = ['file', 'title', 'access']

    # def get_form_kwargs(self):
    #     print(self.request.user)
    #     kwargs = super().get_form_kwargs()
    #     kwargs['author'] = self.request.user
    #     return kwargs

    def get_form_class(self):
        if self.request.user.is_anonymous:
            self.form_class = AnonymCreationForm
        else:
            self.form_class = FileCreationForm
        return self.form_class

    def form_valid(self, form):
        self.object = form.save(commit=False)
        author = self.request.user
        self.object.author_id = author.pk
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:index')


class FilesDeleteView(UserPassesTestMixin, DeleteView):
    model = Files
    template_name = 'delete.html'
    context_object_name = 'files'

    def test_func(self):
        if self.request.user.has_perm('file_change') or self.get_object().author == self.request.user:
            return True

    def get_success_url(self):
        return reverse('webapp:index')


class FilesUpdateView(UserPassesTestMixin, UpdateView):
    model = Files
    template_name = 'files_update.html'
    # form_class = FileCreationForm
    fields = ('title', 'file', 'access')
    context_object_name = 'files'

    def test_func(self):
        if self.request.user.has_perm('file_change') or self.get_object().author == self.request.user:
            return True

    def get_success_url(self):
        # return redirect('accounts:user_detail', pk=self.user_pk)
        return reverse('webapp:index')


class FilesDetailView(DetailView):
    model = Files
    template_name = 'file_detail.html'
    context_object_name = 'files'
# Create your views here.
