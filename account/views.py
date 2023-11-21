from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    
    return request.session.session_key

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            login(request, user)
            return redirect('home')
        #  print(form.cleaned_data)
        
        
    return render(request, 'account/register.html',{'form':form})

def profile(request):
    return render(request, 'account/dashboard.html')

def sign_in(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = user_name, password = password)
        print(user)
        login(request, user)
        
        #login hoye gese
        return redirect('home')
    return render(request, 'account/signin.html')

def user_logout(request):
    logout(request)
    return redirect('sign_in')
