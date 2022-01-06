from django.shortcuts import render

def index(request):
    name = 'Doyeon Kim'
    return render(request, 'index.html', {'my_name' : name})