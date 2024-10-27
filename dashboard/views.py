from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request,'profile.html')

def dashboard(request):
    return render(request,'dashboard.html')