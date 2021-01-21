from django.shortcuts import render,redirect 
from django.contrib import auth
from django.contrib.auth import get_user_model
User = get_user_model()
from mydiary.views import show

# Create your views here.
def login(request):
    if request.method == "POST":
        # check if a user exists
        # with the username and password
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect(show)
        else:
            return render(request, 'login.html', {'error': "User not found!"})
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        # to create a user
        if request.POST['password'] == request.POST['passwordagain']:
            # both the passwords matched
            # now check if a previous user exists
            if User.objects.filter(username=request.POST['username']).exists():
                return render(request, 'register.html', {'error': "Username Has Already Been Taken"})
            elif User.objects.filter(email=request.POST['email']).exists():
                return render(request, 'register.html', {'error': "Email Has Already Been Taken"})
            else:
                user = User.objects.create_user(username= request.POST['username'], email= request.POST['email'], password= request.POST['password'])
                auth.login(request, user)
                return redirect(login)
        else:
            return render(request, 'register.html', {'error': "Passwords Don't Match"})
    else:
        return render(request, 'register.html') 

def logout(request):
    auth.logout(request)
    return redirect(login)