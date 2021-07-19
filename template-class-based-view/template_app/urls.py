from django.urls import path
from django.views.generic import TemplateView, RedirectView
from .views import *

urlpatterns = [

    """ extra_context Attribute  from ContextMixin - keyword argument for as_view()"""
    
    path('post', TemplateView.as_view(template_name='index.html',extra_context={'name': 'Post 1', 'description': 'This is First post about Templateview which is class based view'})),
    path('post1', postView.as_view(),name="post"),
    path('rdt',RedirectView.as_view(url='https://www.google.com/'),name='go-to-google'),
    path('postpreload/<int:pk>',PostPreloadTasktView.as_view(),name='redirect-task'),
    path('singlepost/<int:pk>',SinglePostView.as_view(),name='singlepost')
]
