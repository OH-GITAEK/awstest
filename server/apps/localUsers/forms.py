from django import forms
from .models import LocalUser

class LocalUserForm(forms.ModelForm):
  class Meta():
    model = LocalUser
    fields = ('__all__')