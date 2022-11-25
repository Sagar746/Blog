from django.shortcuts import render,redirect
from .models import Post
from .forms import PostModelForm
# Create your views here.

def index(request):
	posts = Post.objects.all()
	if request.method == 'POST':
		forms = PostModelForm(request.POST)
		if forms.is_valid():
			instance = forms.save()
			instance.author = request.user
			instance.save()
			return redirect('blog-index')
	else:
		forms = PostModelForm()

	context = {
		'posts':posts,
		'forms':forms,
	}
	return render(request, 'index.html', context)


def about(request):
	return render(request, 'about.html')