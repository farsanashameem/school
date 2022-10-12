from django.shortcuts import render

# Create your views here.
def loginfun(request):
    return render(request,'hod_templates/login.html')