"""cash URL Configuration

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
from django.views.generic import TemplateView
from apps.cards.api import CardList, CardDetail, Auth
from rest_framework import routers
from apps.cards.views import IndexView, get_id, add_transaction, logout
# print '-'*10,applications.cards.api
# print '-'*10,applications.cards.api
router = routers.DefaultRouter()
# router.register(r'accounts', UserView, 'list')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view()),
    url(r'^get_id/', get_id),
    url(r'^add_transaction/', add_transaction),
    url(r'^logout/', logout),
    url(r'^test/$', CardList.as_view()),
    url(r'^test/auth/$', Auth.as_view()),
    url(r'^test/(?P<cards_num>[0-9]+)$', CardDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
