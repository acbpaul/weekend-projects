from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Book

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect(reverse("myapp:index"))
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def index(request):
    return render(request, "index.html")

def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {'books':books})