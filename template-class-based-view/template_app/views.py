from django.shortcuts import render,get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from .models import Post
from django.db.models import F
# Create your views here.

class postView(TemplateView):

	""" TemplateResponseMixin
	provides a mechanism to construct a TemplateResponse, given Suitable context.
	Attributes:
	"""
	template_name ='post.html'
	
	# template_engine = the NAME of template engine to use for loading the jinja files
	# response_class = Custom template loading or custom context object instantiation
	# content_type = defaullt Django uses 'text/html'

	"""inherited from ContentMixin """
	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['post'] = Post.objects.get(id=1)
		context['data'] = 'Hello World'
		return context


class PostPreloadTasktView(RedirectView):

	# url = 'https://www.google.com/'
	pattern_name = 'singlepost'

	""" if url is not define then it looks for pattern_name
	"""

	def get_redirect_url(self, * args, **kwargs):
		# post = get_object_or_404(Post,pk=kwargs['pk'])
		# post.count = F('count') + 1
		# post.save()
		post = Post.objects.filter(pk=kwargs['pk'])
		post.update(count=F('count')+1)
		return super().get_redirect_url(*args,**kwargs)

class SinglePostView(TemplateView):

	template_name ='single.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['posts'] = get_object_or_404(Post,pk=self.kwargs.get('pk'))
		return context
