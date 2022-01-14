from django import forms
from django.forms.widgets import TextInput, Textarea
from django.utils.translation import gettext_lazy as _
from . models import Contact

class ContactForm(forms.ModelForm):

	class Meta:
		model = Contact
		fields = '__all__'
		widgets = {
			'name': TextInput(attrs={'class': 'required form-control','placeholder': 'Name'}),
			'email': TextInput(attrs={'class': 'required form-control','placeholder': 'Email'}),	
			'message': Textarea(attrs={'class': 'required form-control','placeholder': 'Message'}),	

		}
		error_messages = {
			'name': {
				'required': _("Name field is required."),
			},
			'email': {
				'required': _("Phone field is required."),
			},
			'message': {
				'required': _("Message field is required."),
			}
		}