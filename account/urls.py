"""marlin URL Configuration

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
#from django.conf.urls import patterns
from django.conf.urls import url
from .views import sign_up

urlpatterns = [
    #url(r'^register/', views.register, name='register'),
    #url(r'^signup$', sign_up.sign_up, name='sign_up'),
]


# urlpatterns = patterns(
#     url(r'^$', views.register, name='register'),

# #     # ex: /polls/
# #     url(r'^$', views.index, name='index'),
# #     # ex: /polls/5/
# #     url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
# #     # ex: /polls/5/results/
# #     url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
# #     # ex: /polls/5/vote/
# #     url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
# )
