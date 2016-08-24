"""ratings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from app.views import LoginView,LogoutView,user_create_view,IndexView,BookCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^$',IndexView.as_view(), name="index_view"),
    url(r'^login/$', login, name="login_view"),
    url(r'^logout/$', logout, name="logout_view"),
    url(r'^book/$',BookCreateView.as_view(), name='book_create_view'),
    url(r'^user_create/$', user_create_view, name='user_create_view')
]
