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
from webapp.forms import FileCreationForm, SimpleSearchForm
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
    # ordering = ['-date']
    # paginate_by = 10
    # paginate_orphans = 1

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(title__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None



class FilesCreateView(CreateView):
    model = Files
    template_name = 'file_create.html'
    fields = ['file', 'title']

    # def get_form_kwargs(self):
    #     print(self.request.user)
    #     kwargs = super().get_form_kwargs()
    #     kwargs['author'] = self.request.user
    #     return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        author = self.request.user
        self.object.author_id = author.pk
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:index')


class FilesDeleteView(DeleteView):
    model = Files
    template_name = 'delete.html'
    context_object_name = 'files'

    def get_success_url(self):
        return reverse('webapp:index')


class FilesUpdateView(UpdateView):
    model = Files
    template_name = 'files_update.html'
    # form_class = FileCreationForm
    fields = ('title', 'file')
    context_object_name = 'files'
    # permission_required = "accounts.change_user"
    # permission_denied_message = "Доступ запрещен"

    # def form_valid(self, form):
    #     pk = self.kwargs.get('pk')
    #     # user = get_object_or_404(User, id=pk)
    #     file = get_object_or_404(Files, file=pk)
    #     print(file.title)
    #     # user = get_object_or_404(User, pk=pk)
    #     # user.first_name = form.cleaned_data['first_name']
    #     file.file = form.cleaned_data['file']
    #     file.title = form.cleaned_data['title']
    #     file.save()
    #     # user.save()
    #     # self.user_pk = self.kwargs['pk']
    #
    #     return self.get_success_url()

    # def test_func(self):
    #     return self.request.user.pk == self.kwargs['pk']

    def get_success_url(self):
        # return redirect('accounts:user_detail', pk=self.user_pk)
        return reverse('webapp:index')


class FilesDetailView(DetailView):
    model = Files
    template_name = 'file_detail.html'
    context_object_name = 'files'
# Create your views here.
