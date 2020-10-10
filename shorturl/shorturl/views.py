# File created by me
from django.http import HttpResponse
from django.shortcuts import render
import pyshorteners

def index(request):
    return render(request, 'index.html')
def shorturl(request):
    txt = request.POST.get('text', 'default')
    print(txt)
    shortener = pyshorteners.Shortener()
    x = shortener.tinyurl.short(txt)
    params = {'purpose':'Url Shortened','analyzed_text':x}
    return render(request, 'shorturl.html',params)