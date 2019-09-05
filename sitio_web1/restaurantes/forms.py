from django import forms
from django.core.exceptions import ValidationError

def codigo_postal(codigo):

	if codigo < 10000 or codigo > 99999:
		raise ValidationError('%s no es un codigo postal valido' % codigo)

class RestauranteForm(forms.Form):
	name = forms.CharField(label='Nombre', max_length=55, strip=True, widget=forms.TextInput(
		attrs={'class':'form-control text-muted col-md-4',
			'size':30}))
	cuisine = forms.CharField(label='Tipo', max_length=55, required=False)

	zipcode = forms.IntegerField(label='Codigo_Postal', validators=[codigo_postal])

class BuscarForm(forms.Form):
	buscar = forms.CharField(label='Buscar', max_length=55, strip=True, widget=forms.TextInput(
		attrs={'class':'form-control text-muted col-md-4',
			'size':30}))
