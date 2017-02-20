"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin

from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # 主页
    url(r'^$', views.home, name='home'),

    # 展示文章的细节
    url(r'^(?P<article_id>\d+)/$', views.detail, name='detail'),

    # About me
    url(r'^me/$', views.about_me, name='about_me'),

    # 联系我
    url(r'^contact/$', views.contact, name='contact'),

    # 以前的文章
    url(r'^pre/$', views.pre, name='pre')

]
