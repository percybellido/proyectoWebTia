from django.urls import path
from .import views
urlpatterns = [
    path('', core_views.home, name='home'),
    path('services/', services_views.services, name='services'),
    path('blog/', core_views.blog, name='blog'),
    path('contact/', core_views.contact, name='contact'),
    path('reviews/', core_views.reviews, name='reviews'),
]
