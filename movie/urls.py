from django.conf.urls import url
from .import views
app_movie='movie'
urlpatterns=[
	url(r'^$', views.home, name='home'),
]