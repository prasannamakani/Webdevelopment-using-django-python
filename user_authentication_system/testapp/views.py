from django.shortcuts import render,redirect
from django.contrib import messages
from testapp.models import People



def index_view(request):
    return render (request,'index.html')

def register_view(request):
    if request.method=='POST':
        username=request.POST['u_name']
        password=request.POST['pass_word']
        email=request.POST['email']
        if People.objects.filter(Username=username).exists():
            messages.error(request, "Username already taken,please choose another")
            return render(request, 'register.html')
        elif People.objects.filter(Email=email).exists():
            messages.error(request, "Email already taken,please choose another")
            return render(request, 'register.html')
        you=People.objects.create(Username=username,Password=password,Email=email)
        you.save()
        return redirect ('/login')

    return render ( request,    'register.html')

def login_view(request):
    if request.method=="POST":
        lusername=request.POST.get('l_name')
        lpassword=request.POST.get('l_pass_word')
        user= People.objects.filter(Username=lusername,Password=lpassword).first()
        if user is not None:
            request.session['username'] = user.Username  
            request.session['email'] = user.Email 
            return redirect('/profile')
        else:
            messages.error(request, "Invalid credentials, please try again")
            return redirect ('/login')

    return render(request,  'login.html')
def profile_view(request):
    username=request.session.get('username')
    email=request.session.get('email')
    
    if username and email:
        return render(request, 'profile.html',{'username':username,'email':email})
    else:
        return redirect ("/login")
# Create your views here.
