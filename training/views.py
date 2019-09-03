from django.shortcuts import render

# Create your views here.
def training(request):
    """ Redeners traning """
    return render(request, 'training.html')