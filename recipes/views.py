from django.shortcuts import render



# Create your views here.

def index(request):
    return render(request,'recipes/recipes_index.html')

def about(request):
    return render(request,'recipes/about.html')

def contact(request):
    return render(request,'recipes/contact.html')
