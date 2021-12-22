from django.shortcuts import render, redirect
from .models import *


def Home(request):
    return render(request, 'home.html')


def Kasb(request):
    kasblar = Kasblar.objects.all()
    context = {
        'kasblar': kasblar,
    }
    return render(request, 'kasb.html', context)


def AddKasb(request):
    name = request.POST['kasb']
    Kasblar.objects.create(name=name)
    return redirect('/kasb/')


def DeleteKasb(request, id):
    kasb = Kasblar.objects.get(id=id)
    kasb.delete()
    return redirect('/kasb/')

def EditKasb(request):
    if request.POST:
        new_kasb = request.POST['kasb']
        kasb_id = request.POST['id']
        current_kasb = Kasblar.objects.get(id=kasb_id)
        current_kasb.name=new_kasb
        current_kasb.save()
        return redirect('/kasb/')
    else:
        kasb_id = request.GET.get('kasb')
        kasb = Kasblar.objects.get(id=kasb_id)
        print(kasb_id, kasb)
        context = {
            'kasblar':Kasblar.objects.all(),
            'kasb':kasb,
        }
        return render(request, 'kasb.html', context)

def Hodim(request):
    return render(request, 'hodim.html')
