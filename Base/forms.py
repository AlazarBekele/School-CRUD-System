from django import forms
from .models import SchoolDeployment

class formInput (forms.ModelForm):
  class Meta:
   model = SchoolDeployment
   fields = '__all__'

   widgets = {
     'first_name' : forms.TextInput(attrs={
       'class' : 'form-control'
     }),
    'last_name' : forms.TextInput(attrs={
       'class' : 'form-control'
     }),
     'description' : forms.Textarea(attrs={
       'class' : 'form-control',
       'type' : 'Text'
     })
   }