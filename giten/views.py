from django.shortcuts import render, get_object_or_404

# Create your views here.

def index(request):

    return render(request, 'giten/giten_home.html')

def giten_ncreate(request):

    return render(request, 'giten/giten_ncreate.html')
