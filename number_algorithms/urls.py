from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^findpi/$', views.find_pi, name='find_pi'),
    # url(r'^findpi/(?P<pi>\d+)/$', views.find_pi, name='find_pi'),
    url(r'^findpi/sendn$', views.find_pi, name='pi_to_n'),
]
