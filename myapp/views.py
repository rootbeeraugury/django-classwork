from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return HttpResponse("<h1>Hello Django!</h1>")

def about(request):
  return HttpResponse("<h1>About Page!</h1> <br> <h5>This is an about page.</h5>")

def fourohfour(request):
  return HttpResponse("<h1>404 Error (faked)</h1>")