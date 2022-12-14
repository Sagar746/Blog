from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

	def __init__(self, *args, **kwargs):
		super(UserRegistrationForm, self).__init__(*args,**kwargs)

		for fieldname in ['username','email','password1','password2']:
			self.fields[fieldname].help_text = None