from django.shortcuts import render
from accounts.models import *

# Create your views here.
def index(request):
    is_HR = request.user.groups.filter(name='HR').exists()
    return render(request, 'dashboard_index.html',{'is_HR':is_HR})

def recordNotFound(request):
    return render(request,'recordNotFound.html')