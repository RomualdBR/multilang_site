from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')  # Assurez-vous d'avoir un template 'home.html'
