from django.shortcuts import render,redirect
from .models import Todolist
def home(request):
    dblist=Todolist.objects.all()
    n=len(dblist)
    context={'context':dblist,'n':n}
    return render(request,'todo/home.htm',context)
def send(request):
    if request.method=="POST":
        mylist=request.POST.get('list')
        alllist=Todolist(mylist=mylist)
        alllist.save()
    return redirect("/")      
       

     

    

