from django.shortcuts import render

# Create your views here.
def index(request):

    return render(request, 'myapp/index.html')


def throw(request):
    return render(request,'myapp/throw.html')

def catch(request):
    return render(request,'myapp/catch.html')
