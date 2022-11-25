from django.urls import path
from .views import index,about

urlpatterns = [
	path('blog/', index, name='blog-index'),
	path('about/', index, name='blog-about'),
]