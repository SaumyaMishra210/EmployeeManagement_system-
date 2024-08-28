from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import UserSignupForm
from .models import *
from django.contrib.auth import authenticate, login



def signup(request):
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
                    AdminProfile.objects.create(user_profile=user_profile )
                elif role == 'HR':
                    hr_group = Group.objects.get(name='HR')
                    user.groups.add(hr_group)
                    HRProfile.objects.create(user_profile=user_profile)
                elif role == 'Manager':
                    manager_group = Group.objects.get(name='Manager')
                    user.groups.add(manager_group)
                    ManagerProfile.objects.create(user_profile=user_profile)
                elif role == 'Employee':
                    employee_group = Group.objects.get(name='Employee')
                    user.groups.add(employee_group)
                    EmployeeProfile.objects.create(user_profile=user_profile)
            else:
                messages.error(request, 'Registration FAILED.')

            # Log in the user after successful registration (optional)
            # login(request, user)
            messages.success(request, 'Registration successful.')

            return redirect('index')  # Redirect to a home page or dashboard after signup
    else:
        form = UserSignupForm()

    return render(request, 'signup.html', {'form': form})


def userlogin(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        eid = request.POST.get('eid')

        # Check if 'eid' is provided (for employees)
        if eid:
            user = authenticate(request, eid=eid, password=password)
        else:
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to a home page or dashboard after login
        else:
            messages.error(request, 'Invalid login credentials.')

    return render(request, 'login.html')
