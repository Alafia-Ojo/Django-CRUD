from dataclasses import fields
from msilib.schema import ListView
from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.edit import CreateView




class PostListView: 
    model = Post
    


class PostCreateView(CreateView):
   model = Post
   fields="__all__"
   success_url = reverse_lazy("blog:all")

class PostDetailView: 
    model = Post
   
    
class PostUpdateView(UpdateView): 
    model = Post
    fields="__all__"
    success_url = reverse_lazy("blog:all")   
