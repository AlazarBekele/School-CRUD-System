from django import forms
from .models import School_Deployment

class formInput (forms.ModelForm):
  class Meta:
   model = School_Deployment
   fields = '__all__'

   widgets = {
     'first_name' : forms.TextInput(attrs={
       'class' : 'form-control'
     }),
    'last_name' : forms.TextInput(attrs={
       'class' : 'form-control'
     })
   }