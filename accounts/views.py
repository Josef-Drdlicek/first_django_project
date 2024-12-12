from django.shortcuts import render, redirect
from .forms import UserRegisterForm, DataEntryForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import DataEntry
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Zahashuje heslo
            user.save()
            messages.success(request, f"Účet byl vytvořen pro {user.username}")
            return redirect('login')  # Přesměrování na login po registraci
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Přesměrování po přihlášení
            else:
                messages.error(request, "Chybné uživatelské jméno nebo heslo")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def home(request):
    return render(request, 'accounts/home.html')

@login_required
def add_data(request):
    if request.method == 'POST':
        form = DataEntryForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            messages.success(request, "Data byla úspěšně uložena!")
            return redirect('home')  # Dočasně na home, než vytvoříme tabulku
    else:
        form = DataEntryForm()
    return render(request, 'accounts/add_data.html', {'form': form})

@login_required
def data_table(request):
    query = request.GET.get('q')  # Získání hodnoty filtru z GET parametrů
    if query:
        data_entries = DataEntry.objects.filter(user=request.user, title__icontains=query).order_by('-created_at')
    else:
        data_entries = DataEntry.objects.filter(user=request.user).order_by('-created_at')
    
    return render(request, 'accounts/data_table.html', {'data_entries': data_entries, 'query': query})

def logout_view(request):
    logout(request)  # Odhlásí uživatele
    return redirect('login')  # Přesměruje na přihlašovací stránku

def about(request):
    return render(request, 'accounts/about.html')


