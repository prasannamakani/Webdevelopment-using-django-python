from django.shortcuts import render,redirect
from django.contrib import messages
from testapp.models import People,JobApplication
from datetime import date


def register_view(request):
    if request.method=='POST':
        username=request.POST['user_name']
        password=request.POST['pass_word']
        confirm_password=request.POST['confirm_pass_word']
        if People.objects.filter(Username=username).exists():
            messages.error(request, "Username already taken,please choose another")
            return render(request, 'templates/register.html')
        elif People.objects.filter(Password=password).exists():
            messages.error(request, "Password already taken,please choose another")
            return render(request, 'templates/register.html')
        you=People.objects.create(Username=username,Password=password,Confirm_Password=confirm_password)
        you.save()
        return redirect ('index')

    return render(request, 'register.html')

def index_view(request):
    if request.method == "POST":
        lusername = request.POST.get('l_username', '').strip()
        lpassword = request.POST.get('l_pass_word', '').strip()

        if not lusername or not lpassword:  
            messages.error(request, "Username and Password are required.")
            return redirect('index')

        print(f"Trying to login with: {lusername}, {lpassword}")  

        user = People.objects.filter(Username=lusername).first()

        if user:
            print(f"User found: {user.Username}, Stored Password: {user.Password}")  
            if user.Password == lpassword:
                print("Password matched! Redirecting to home.")
                request.session['username'] = user.Username  
                return redirect('home')
            else:
                print("Password does not match.")
        
        print("No matching user found.") 
        messages.error(request, "Invalid credentials, please try again")
        return redirect('index')

    return render(request, 'index.html')

def home_view(request):
    if request.method == "POST":
        company = request.POST.get("Company")
        position = request.POST.get("Position")
        ctc = request.POST.get("Ctc") 
        date_applied = request.POST.get("Date")

       
        if not date_applied:
            date_applied = date.today()

       
        JobApplication.objects.create(
            Company=company,
            Position=position,
            Ctc=ctc if ctc else None,  
            Date=date_applied
        )

        return redirect('home') 

    return render(request,'home.html')

# Create your views here.
