from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    f = {'name' : ['Joyant', 'Sheikhar', 'Gupta', 'Joy'], 
         'date' : datetime.datetime.now(),
         'val' : '', 
         'valu' : '20',
         'nm' : 'joyant'
         }
    return render(request, 'home.html', f)