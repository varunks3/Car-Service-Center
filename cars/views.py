from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    return render(request,'home/index.html')

def aboutUs(request):
    return render(request,'home/About Us.html')

def contact(request):
    return render(request,'home/Contact.html')


def signup(request):
    if request.method == 'POST':
        fName = request.POST['fname']
        lName = request.POST['lname']
        userName = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username = userName, password = password, email = email, first_name = fName, last_name = lName)
        print('account created')
        return redirect('/login')
    else:
        return render(request,'home/signup.html')



# def index(request):
#     if request.method == 'POST':
        
#     return HttpResponse('Hey, there')


def login(request):
    if request.method == 'POST':
        userName = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = userName, password = password)

        if user is not None:
            auth.login(request, user)
            print('Logged in')
            return redirect('/')
    else:
        return render(request,'home/login.html')