
from django.conf.urls import url

from . import views


app_name = 'polls'

urlpatterns = [
    #리스트뷰는 똑같은 것만 보여주는 페이지 이기 때문에 파라미터를 받지 않는다.
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = "detail"),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name = "results"),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name = "vote"),

    #url(r'^$', views.index, name = 'index'),
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name = "detail"),
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name = "results"),
]
