from django.shortcuts import render
def skill(request):
    content={'skill':'active'}
    return render(request,'edu/skill.htm',content)
