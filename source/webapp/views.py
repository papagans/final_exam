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
from webapp.forms import FileCreationForm
from webapp.models import Files
# Create your views here.


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'files'
    model = Files
    # ordering = ['-created_at']


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
