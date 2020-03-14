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
# from webapp.forms import AnnounceCreationForm, ImagesCreationForm
# from webapp.models import Announce, Favorite, Images
# Create your views here.


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'announce'
    model = User
    ordering = ['-created_at']
# Create your views here.
