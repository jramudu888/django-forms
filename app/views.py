from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse
# Create your views here.
def insert_school(request):
    sf=SchoolForm()
    d={'sf':sf}
    if request.method=='POST':
        FD=SchoolForm(request.POST)
        if FD.is_valid():
            id=FD.cleaned_data.get('id')
            name=FD.cleaned_data.get('name')
            S=School.objects.get_or_create(Sid=id,Sname=name)[0]
            S.savs()
            return HttpResponse('School is created successfully')
    return render(request,'insert_school.html',d)

def sample(request):
    form=SampleForm()
    d={'form':form}
    return render(request,'sample.html',d)