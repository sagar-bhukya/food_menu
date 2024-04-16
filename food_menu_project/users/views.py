from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm
from .models import Profile

from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':#represents the HTTP request sent to the server.
        form = RegisterForm(request.POST)#request.POST: This contains all the data sent through the form in the POST request.
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f'{username} account has been created successfully! Please log in.')
                return redirect('login')
            else:
                messages.error(request, 'Login failed. Try again.')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

# def login_user(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user:
#             login(request, user)
#             messages.success(request, f'{username} have successfully logged in.')
#             return redirect('index')
#         else:
#             messages.error(request, 'Invalid username or password')
#     else:
#         return render(request, 'users/login.html')
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to a home page or appropriate URL
        else:
            # Return an error message to the login page
            return render(request, 'users/login.html', {'error': 'Invalid username or password'})
    else:
        # GET request: just show the login form
        return render(request, 'users/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return render(request, 'users/logout.html')

@login_required #restrict for profile after logout you need to login for.
#for profile those who are register and login then only it will display the home page
def profilepage(request):
    get_profile=Profile.objects.all()
    context={
        "get_profile":get_profile
    }
    return render(request,'users/profile.html',context)
    #after runserver by defualt  http://127.0.0.1:8000/accounts/login/?next=/profile/   we dont want accounts so got settings add login_url path
