from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator
from django.http import Http404

from Base.permissions import is_HR
from accounts.models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserDetails
from .forms import UserDetailsForm


# Create your views here.
# def index(request):
#     # is_HR = request.user.groups.filter(name='HR').exists()
#     return render(request, 'dashboard_index.html',{'is_HR':is_HR})



def is_hr(user):
    return user.groups.filter(name='HR').exists()
from django.core.paginator import Paginator

@login_required
@user_passes_test(is_hr)
def user_details_list(request):
    users = UserDetails.objects.all()
    paginator = Paginator(users, 3)  # Show 3 users per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'user_details_list.html', {'page_obj': page_obj})

@login_required
@user_passes_test(is_hr)
def user_details_create(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_details_list')
    else:
        form = UserDetailsForm()
    return render(request, 'user_details_form.html', {'form': form})

@login_required
@user_passes_test(is_hr)
def user_details_edit(request, pk):
    user_detail = get_object_or_404(UserDetails, pk=pk)
    if request.method == 'POST':
        form = UserDetailsForm(request.POST, instance=user_detail)
        if form.is_valid():
            form.save()
            return redirect('user_details_list')
    else:
        form = UserDetailsForm(instance=user_detail)
    return render(request, 'user_details_form.html', {'form': form})

@login_required
@user_passes_test(is_hr)
def user_details_delete(request, pk):
    user_detail = get_object_or_404(UserDetails, pk=pk)
    if request.method == 'POST':
        user_detail.delete()
        return redirect('user_details_list')
    return render(request, 'user_details_confirm_delete.html', {'user_detail': user_detail})

@login_required
def user_details_view(request):
    # user_detail = get_object_or_404(UserDetails, user=request.user)
    try:
        user_detail = get_object_or_404(UserDetails, user=request.user)
    except Http404:
        return redirect('recordNotFound')
    if not is_HR and request.user == 'admin':
        # raise PermissionDenied
        return redirect('recordNotFound')
    context = {
        'user_detail': user_detail,
        'is_HR':is_hr(request.user),
    }
    return render(request, 'user_details_view.html', context)

@login_required
def user_details_edit_self(request):
    user_detail = get_object_or_404(UserDetails, user=request.user)
    if request.method == 'POST':
        form = UserDetailsForm(request.POST, instance=user_detail)
        if form.is_valid():
            form.save()
            return redirect('user_details_view')
    else:
        form = UserDetailsForm(instance=user_detail)
    return render(request, 'user_details_form.html', {'form': form})
