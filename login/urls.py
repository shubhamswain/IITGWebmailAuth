from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^home/', views.home, name='home'),
	url(r'^login/', views.login_user, name='login'),
	url(r'^$', views.login_user, name='login'),

]