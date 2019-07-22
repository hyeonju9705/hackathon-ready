from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('site')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'register.html', 
                      {'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('blog')
        else:
            return render(request, 'register.html', 
                  {'error': 'Passwords must match'})
    else:
        return render(request, 'register.html')

                                      
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('site')
    return render(request,'signup.html')



            
