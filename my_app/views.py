from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
   return render(request, 'home.html')

def index2(request):
   return render(request, 'form.html')
