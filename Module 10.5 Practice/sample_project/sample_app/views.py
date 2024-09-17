from django.shortcuts import render

# Create your views here.
def home(request):
    f = {'name' : ['Joyant', 'Sheikhar', 'Gupta', 'Joy']}
    return render(request, 'home.html', f)