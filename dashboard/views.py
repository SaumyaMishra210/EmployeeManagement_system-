from django.shortcuts import render
from accounts.models import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recordNotFound(request):
    return render(request,'recordNotFound.html')