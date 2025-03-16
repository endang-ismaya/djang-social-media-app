from django.shortcuts import render

# Create your views here.

def index(request):
    """account index view"""
    context = {}
    return render(request, "account/index.html", context)
