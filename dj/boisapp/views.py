from cgitb import text
from django.shortcuts import render
from django.http import HttpResponse
from .models import summarizer
text=""
# Create your views here.
def home(request):
    return render(request,'front.html')

def register(request):
    if request.method== "POST":
        #url=""
        url=request.POST.get('url')
        return render(request,'index.html',
                      {'url':summarizer(url)})
