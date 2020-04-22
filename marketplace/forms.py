from django import forms
from .models import Advert

class AdForm(forms.ModelForm):
	class Meta:
		model = Advert
		exclude=('slug','user')
