"""Users view"""
# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def login_view(request):
    """Login view"""
    if request.user.is_authenticated:
        return redirect("feed")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')