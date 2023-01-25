from django.shortcuts import render, redirect
from .forms import CreateNewEvent
from .models import Room, Event

# Create your views here.
def index(request):
    if request.method=="GET":
        #Muetra la interfaz 
        return render(request, "index.html", {
            "event": CreateNewEvent()
        })
        
    else:
        print(request.POST)
        Room.objects.create(titleRoom=request.POST["titleRoom"], passwordRoom=request.POST["passwordRoom"])
        return redirect("/home/")
        
        

def login(request):
    return render(request, "user_sesion/login.html")

def signin(request):
    return render(request, "user_sesion/signin.html")

def eventManage(request):
    return render(request, "event_manage.html")