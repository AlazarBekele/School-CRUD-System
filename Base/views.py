from django.shortcuts import render
from .models import (
    School_Deployment,
    Catagory,
)
from django.contrib import messages
from .forms import formInput
# Create your views here.

def index (request):

    form = formInput (request.POST or None)
    if request.method == 'POST':
        
      form.is_valid
      form.save()
      messages.success (request, 'Successfully Deployed!')

      form = formInput()

    form_database = School_Deployment().objects.all()

    context = {
        'form_database' : form_database,
        'form' : form
    }

    return render (request, 'Base/index.html', context)