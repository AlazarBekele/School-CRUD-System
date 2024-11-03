from django.shortcuts import render, HttpResponse, redirect
from .models import SchoolDeployment
from django.contrib import messages
from .forms import formInput
# Create your views here.



def index (request): # Create
    form = formInput (request.POST or None)

    if request.method == 'POST':

      if form.is_valid():
        form.save()
        messages.success (request, 'Successfully Deployed!')
        form = formInput()

    schoolData = SchoolDeployment.objects.all()
    context = {
        'schoolData' : schoolData,
        'form' : form
    }

    return render (request, 'Base/index.html', context=context)


def detailOwn (request, id): # Update & Delete
    
    try:
      schoolid = SchoolDeployment.objects.get(pk=id)
    except:
      return HttpResponse ('Bad request!')
    
    form = formInput(request.POST or None, instance=schoolid)

    if request.method == 'POST':
        form.save()
        messages.success (request, 'Successfully Updated!')
        return redirect ('index')
    
    context = {
       'schoolid' : schoolid,
       'form' : form
    }

    return render (request, 'Base/detail.html', context=context)