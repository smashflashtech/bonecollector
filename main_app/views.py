from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  # return HttpResponse('<h1>GET READY TO COLLECT SOME BONES</h1>')
  return render(request, 'index.html')

def about(request):
  # return HttpResponse('<h1>About the Bone Collector</h1>')
  return render(request, 'about.html')

def bones_index(request):
  return render(request, 'bones/index.html', {'bones': "null"})