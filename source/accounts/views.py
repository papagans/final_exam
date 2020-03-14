from django.shortcuts import render

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import UpdateView, DetailView, ListView, DeleteView, FormView, CreateView
# from accounts.models import Profile
from accounts.forms import UserCreationForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin

# from webapp.models import Announce


def login_view(request, *args, **kwargs):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect('webapp:index')
        else:
            context['has_error'] = True
            context['next'] = next_url
            context['username'] = username
    else:
        context = {'next': request.GET.get('next')}
    return render(request, 'register.html', context=context)


def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('webapp:index')


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            user.set_password(form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect(reverse('accounts:user_detail', kwargs={"pk": user.pk}))
    else:
        form = UserCreationForm()
    return render(request, 'register.html', context={'form': form})


class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    ordering = ["user_announce_created_at"]
# Create your views here.
