from django.shortcuts import get_object_or_404, render

from market.models import Fruty

def fruty_detail(request,pk):
    fruty=get_object_or_404(Fruty,pk=pk)
    context={
        'fruty':fruty,
    }
    return render(request,'fruty_detail.html',context)
