from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group

from Base.permissions import is_HR, is_Employee
from .forms import UserSignupForm
from .models import *
from django.contrib.auth import authenticate, login


def signup(request):
    is_Employee = request.user.groups.filter(name='Employee').exists()
    if is_Employee:
        raise PermissionDenied("Access Denied: You do not have permission to access this page.")

    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            role = form.cleaned_data['role']

            # Save the user to the database
            user.save()

            # Create UserProfile instance
            user_profile = UserProfile.objects.get(user=user)
            if user_profile:

                # Assign the user to the selected role
                if role == 'Admin':
                    admin_group = Group.objects.get(name='Admin')
                    user.groups.add(admin_group)
                    AdminProfile.objects.create(user_profile=user_profile)
                elif role == 'HR':
                    hr_group = Group.objects.get(name='HR')
                    user.groups.add(hr_group)
                    HRProfile.objects.create(user_profile=user_profile)
                elif role == 'Employee':
                    employee_group = Group.objects.get(name='Employee')
                    user.groups.add(employee_group)
                    EmployeeProfile.objects.create(user_profile=user_profile)
            else:
                messages.error(request, 'Registration FAILED.')

            # Log in the user after successful registration (optional)
            # login(request, user)
            messages.success(request, 'Registration successful.')

            return redirect('user_details_view')  # Redirect to a home page or dashboard after signup
    else:
        form = UserSignupForm()

    return render(request, 'signup.html', {'form': form})


def userlogin(request):
    if request.user.is_authenticated:
        return redirect('user_details_view')

    if request.method == 'POST':
        eid = request.POST.get('eid')
        password = request.POST.get('password')

        if eid:
            # Handle special case for admin login
            if eid == 'admin':
                user = authenticate(request, username=eid, password=password)
                if user is not None and user.is_staff:  # Check if the user is admin and has staff status
                    login(request, user)
                    return redirect('user_details_view')  # Redirect to the admin panel

            # Employee, HR, Manager login with eid
            user = authenticate(request, eid=eid, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, ' Login Successful.')
                return redirect('user_details_view')  # Redirect to a custom dashboard view
            else:
                messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')


def userlogout(request):
    logout(request)
    return redirect('login')
