from django.shortcuts import render
from django.http import HttpResponse
from custom import signals
# Create your views here.
def home(request):
	signals.notification.send(sender=None,request=request,user=['Python','Django'])
	return HttpResponse("This is Home Page")

def index(request):
	return HttpResponse("This is the Index Page")