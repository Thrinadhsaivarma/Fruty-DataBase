from django.shortcuts import render

from market.models import Fruty


def home(request):
    frutys=Fruty.objects.all()
    context={
        'frutys':frutys,
    }

    return render(request,'home.html',context)
