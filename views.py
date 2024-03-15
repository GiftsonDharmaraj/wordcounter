from django.shortcuts import render
from django.http import HttpResponse


# Create your views here...
def index(request):
    return render(request,'templates.html')
def counter(request):
    texter=request.GET['text']
    amount_of_text=len(texter.split())
    return render(request,'counter.html',{'amount':amount_of_text})