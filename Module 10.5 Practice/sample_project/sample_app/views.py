from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    f = {'name' : ['Joyant', 'Sheikhar', 'Gupta', 'Joy'], 
         'date' : datetime.datetime.now(),
         'val' : '', 
         'valu' : '20',
         'nm' : 'joyant',
         'string' : 'Python Is Fun',
         'details' : [
            {'name': 'Josh', 'age': 19},
            {'name': 'Dave', 'age': 22},
            {'name': 'Joe', 'age': 31},
         ],
         'es' : '<p>You are <em>pretty</em> smart!</p>' ,
         'fruit' : ['Apple', 'Mango', 'Orange'],
         'ani' : """cat\ndog\nhorse""",
         'ttl' : 'It is a title'
         }
    return render(request, 'home.html', f)