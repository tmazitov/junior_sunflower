from ..models import Company
from django.forms import ModelForm, TextInput, PasswordInput

class CompanyForm(ModelForm):
	class Meta:
		model = Company
		
		fields = ['name', 'LLC_Number', 'email', 'password']
		# exclude = ['id'] not neccessary to explicitly exclude id

		widgets = {
			"name": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Your company name'
			}),
			"LLC_Number": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Your company LLC'
			}),
			"email": TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'example@mail.com'
			}),
			"password": PasswordInput(attrs={
				'class': 'form-control',
				'placeholder': 'password1234'
			}),
		}