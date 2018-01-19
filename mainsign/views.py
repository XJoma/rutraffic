from django.shortcuts import render

def mainsign(request):
    return render(request, 'mainsign.html', locals())
