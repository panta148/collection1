from django.shortcuts import render
def home(request):
    content={'home':'active'}
    return render(request,'core/home.htm',content)

def contact(request):
    content={'contact':'active'}
    return render(request,'core/contact.htm',content)