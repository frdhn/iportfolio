from django.shortcuts import render

# Create your views here.
def old(request):
    return render(request,"one.html")

def new(request):
    return render(request,"two.html")

def portfolio(request):
    return render(request,"index.html")