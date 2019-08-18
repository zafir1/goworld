from django.urls import reverse

from .models import Interest
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class InterestListView(LoginRequiredMixin,ListView):
    model = Interest
    template_name = 'interest/show.html'
    context_object_name = 'interests'
    ordering = ['interest_name']

class UserInterestListView(LoginRequiredMixin,ListView):
    model = Interest
    template_name = 'interest/show.html'
    context_object_name = 'interests'
    ordering = ['interest_name']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Interest.objects.filter(author=user).order_by('interest_name')


class InterestCreateView(CreateView):
    model = Interest
    fields = ['interest_name']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('my-interest-list')


