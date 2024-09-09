from django.shortcuts import render, redirect

def base(request):
    is_HR = request.user.groups.filter(name='HR').exists()
    return render(request,'base.html',{'is_HR':is_HR})

def home(request):
    if request.user.is_authenticated:
        return redirect('user_details_view')
    return render(request, 'landing_page.html')


def recordNotFound(request):
    return render(request,'recordNotFound.html')