from django.shortcuts import render, HttpResponse, redirect
from .models import (
    School_Deployment,
    Catagory
)

from django.contrib import messages
from .forms import formInput
# Create your views here.

def index (request):
    form = formInput (request.POST or None)

    if request.method == 'POST':
        
      if form.is_valid():
         
        form.save()
        messages.success (request, 'Successfully Deployed!')
        form = formInput()

    school = School_Deployment.objects.all()
    
    context = {
        'school' : school,
        'form' : form
    }

    return render (request, 'Base/index.html', context)


def detailOwn (request, id):
    
    try:
      schoolid = School_Deployment.objects.get(id=id)
    except:
      return HttpResponse ('Bad request!')
    
    form = formInput(request.POST or None, instance=schoolid)

    if request.method == 'POST':
        form.save()
        messages.success (request, 'Successfully Updated!')
        return redirect ('index')
    
    context = {
       'school' : schoolid,
       'form' : form
    }

    return render (request, 'detail.html', context=context)