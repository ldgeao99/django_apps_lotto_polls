
from django.conf.urls import url

from . import views


app_name = 'polls'

urlpatterns = [
    url(r'^main/$', views.main, name='main'),
    url(r'^$', views.IndexView.as_view(), name = 'index'), #ListView는 내부에서 지정한 객체들을 가져오므로 파라미터를 받지 않는다.
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "detail"),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name = "results"),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = "vote"),

    #url(r'^$', views.index, name = 'index'),
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name = "detail"),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name = "results"),
]