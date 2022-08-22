from django.shortcuts import render
def service(request):
    content={'service':'active'}
    return render(request,'serv/service.htm',content)
