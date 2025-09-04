from django.shortcuts import render

def home(request):
    print ("Acessando a home")

    context = {
        'title': 'Home'
    }

    return render(request, 'home.html', context )