from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.
def login_page(request):

    if request.method == "POST":

        if request.POST.get('login_button'):

            username_ = request.POST.get('username')
            password_ = request.POST.get('password')

            user = auth.authenticate(username = username_,password = password_)

            if user is not None:
                auth.login(request,user)
                return redirect('note_book_user:dashboard')
            else:
                messages.error(request,'Invalid Credentials/User not registered')
                return redirect('note_book_user:login_page')

    return render(request,"login.html")

def dashboard(request):
    return render(request, "dashboard.html")
def signup(request):

    if request.method == "POST":

        if request.POST.get('sign_up'):
            #clicked sign up button

            username_ = request.POST.get('username')
            password_ = request.POST.get('password')
            confirm_password_ = request.POST.get('confirm_password')

            if password_ == confirm_password_:
                if User.objects.filter(username = username_).exists():
                    pass
                else:
                    user = User.objects.create(username = username_,password = password_)
                    user.save()
                    messages.success(request,"User created successfully")
                    return redirect('note_book_user:login_page')
            else:
                messages.error(request,"Password did not match")
                return redirect('note_book_user:signup')
            


            


    return render(request,"signup.html")