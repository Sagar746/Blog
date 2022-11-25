from django.shortcuts import render,redirect
from .forms import UserRegistrationForm


# Create your views here.

def sign_up(request):
	if request.method == 'POST':
		forms = UserRegistrationForm(request.POST)
		if forms.is_valid():
			forms.save()
			return redirect('blog-index')
	else:
		forms = UserRegistrationForm()

	context = {
		'forms':forms,
	}
	return render(request,'users/sign_up.html', context)

def profile(request):
	return render(request,'users/profile.html')