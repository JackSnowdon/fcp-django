from django.shortcuts import render, reverse, redirect
from .models import *
# Create your views here.
def index(request):
    """return the index html.file"""
    banner = BannerPost.objects.all()
    return render(request, 'index.html', {"banner":banner})