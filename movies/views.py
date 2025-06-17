from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'movies': ['Good Boy', 'The Blacklist', 'Criminal minds', 'The lincoln lawyer', 'The Walking Dead']
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html', {})