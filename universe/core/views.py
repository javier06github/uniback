from django.shortcuts import render

# Create your views here.
def home(request):
    return render (request,"core/home.html") 

def news(request):
    return render (request,"core/news.html")

