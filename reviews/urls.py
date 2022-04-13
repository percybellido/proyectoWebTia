from django.urls import path
from .views import ReviewsListView, ReviewsCreate


reviews_patterns = ([
    
    path('', ReviewsListView.as_view(), name='reviews'),
    path('create/', ReviewsCreate.as_view(), name='create')
    
],'reviews')