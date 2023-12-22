from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
def country(request):
    QLTO=Country.objects.all()
    d={ "DATA":QLTO }
    return render(request,'country.html',d)

def state(request):
    QLSO=State.objects.all()
    QLSO=State.objects.all().order_by("sname")
    QLSO=State.objects.all().order_by("-sname")
    QLSO=State.objects.all().order_by(Length('sname'))
    QLSO=State.objects.all().order_by(Length('sname').desc())
    QLSO=State.objects.all().filter(sid__gt=4)
    QLSO=State.objects.all().filter(sid__lt=5)
    QLSO=State.objects.all().filter(sid__lte=3)
    QLSO=State.objects.all().filter(sid__gte=2)
    QLSO=State.objects.all()
    d={'data1': QLSO}
    return render(request,'state.html',d)
def insert_country(request):
    coi=int(input('Enter the cid value :'))
    con=input('Enter the  cname :')
    pl=int(input('Enter the cpl :'))
    VCO=Country.objects.get_or_create(cid=coi,cname=con,cpl=pl)[0]
    VCO.save()
    QLCO=Country.objects.all()
    d={ 'data':QLCO }
    return HttpResponse('Country is created')


