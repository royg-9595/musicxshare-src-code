from audioop import reverse
from typing import Optional
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy

def home(request):
    conte ={
        'post':Post.objects.all(),
        'title':'emo-emo'
    }
    return render(request, 'home.html', conte)

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name= 'home.html'
    context_object_name = 'post'
    ordering= ['-date_posted']

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name='post_detail.html'
    context_object_name='i'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields=['title', 'content', 'file']
    template_name= 'post_form.html'

    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields=['title', 'content', 'file']
    template_name= 'post_form.html'

    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)
    
    def test_func(self) -> bool | None:
        i=self.get_object()
        if self.request.user == i.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name='i'
    template_name='post_delete.html'
    success_url='/'

    def test_func(self) -> bool | None:
        i=self.get_object()
        if self.request.user == i.author:
            return True
        return False

@login_required
def about(request):
    context = {
        'title':"Jayanth"
    }
    return render(request,'about.html',context)