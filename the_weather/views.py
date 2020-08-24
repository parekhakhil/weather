from django.shortcuts import render
import requests

# Create your views here.

def index(request):
    url = 'http://api.openeathermap.org/data/2.5/weather?q={}&appid=5df54403085140ed10e3671830333a42'
    return render(request,'home.html')
