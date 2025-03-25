from django.shortcuts import render

# Create your views here.

def index(request):
    """images index view"""
    context = {}
    return render(request, "images/index.html", context)
