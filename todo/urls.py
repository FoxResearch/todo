from django.conf.urls import url
from . import views

app_name = 'todo'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^login/(?P<accion>[0-1]+)$', views.loginval, name='loginval'),
    url(r'^login/exit/$', views.logindel, name='logindel'),
    url(r'^register/$', views.register, name='register'),
    url(r'^register/(?P<accion>[0-1]+)$', views.registerval, name='registerval'),
    url(r'^create/$', views.create, name='create'),
    url(r'^create/(?P<id>[0-9999999999]+)$', views.createval, name='createval'),
    url(r'^list/$', views.list, name='list'),
    url(r'^edit/(?P<id>[0-9999999999]+)$', views.edit, name='edit'),
    url(r'^edit/change/(?P<id>[0-9999999999]+)$', views.editval, name='editval'),
    url(r'^delete/(?P<id>[0-9999999999]+)$', views.delete, name='delete'),
    url(r'^edituser/$', views.edituser, name='edituser'),
    url(r'^edituser/change/$', views.edituserval, name='edituserval')
    # url(r'^$', views.RegisterView.as_view(), name='register')
    # ex: /polls/5/
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]
