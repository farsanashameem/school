from django.shortcuts import render

# Create your views here.
def logfun(request):
    return render(request,'students_templates/login.html')