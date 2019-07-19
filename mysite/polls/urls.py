from django.urls import path

from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
               #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/traffic/$', views.traffic, name='traffic'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/visits/$', views.visits, name='visits'),
    url(r'^(?P<question_id>[0-9]+)/customers/$', views.customers, name='customers'),
    url(r'^(?P<question_id>[0-9]+)/new/$', views.new, name='new'),
    url(r'^(?P<question_id>[0-9]+)/returning/$', views.returning, name='returning'),
    url(r'^(?P<question_id>[0-9]+)/averagestay/$', views.averagestay, name='averagestay'),
]
