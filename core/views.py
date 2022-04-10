from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/home.html')


    



    
def reviews(request):
    return render(request, 'core/reviews.html')
    