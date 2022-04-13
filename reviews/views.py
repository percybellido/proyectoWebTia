from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from .models import Reviews

# Create your views here.
class  ReviewsListView(ListView):
    model=Reviews
    
class ReviewsCreate(CreateView):
    model=Reviews
    fields=['name','email','message','image']
    
    success_url=reverse_lazy('reviews:reviews')