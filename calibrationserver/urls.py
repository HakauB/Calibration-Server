"""calibrationserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.contrib.auth import views as auth_views

import contacts.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login$', auth_views.login, name='login',),
    url(r'^logout/$', auth_views.logout, name='logout',),
    url(r'^$', contacts.views.ListContactView.as_view(), name='contacts-list',),
    url(r'^new$', contacts.views.CreateContactView.as_view(), name='contacts-new',),

]