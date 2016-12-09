from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views

urlpatterns = [
    url(r'^$', include('login.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', include('login.urls')),
    url(r'^logout/$', views.logout, {'next_page': '/login/'}),  
    ]