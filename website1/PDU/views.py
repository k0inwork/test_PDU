from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import PDU
from pip._internal import req

# Create your views here.
def pdu_view(request):
    pdus = PDU.objects.all()

    c = {'pdus': pdus}
    return render(request,"index.html",c)

def pdu_switchoff(request):
    id1=request.GET["id"]
    pdu = PDU.objects.get(id=id1)
    if pdu:
        pdu.state = "Unavailable";
        pdu.save();
        
    return redirect("/site/pdus")
