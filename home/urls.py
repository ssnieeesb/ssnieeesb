from home import views
from django.conf.urls import url
from .models import events
import os
import urllib.request as urllib
app_name = 'home'
from bs4 import BeautifulSoup

import requests
# base_url = "https://gitcdn.link/cdn/KarthikRaja2k1/ieeesb_public/master/home_templates/"
# if(requests.get(base_url+'check.html').content.decode('utf-8')!='404: Not Found'):
#     template_folder='home/templates/'
#     files=os.listdir(template_folder)

#     for file in files:
#         f=open(template_folder+file,"r+")
#         s=""
#         html_content=requests.get(base_url+file)
#         f.write(html_content.content.decode("utf-8"))

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about$', views.about, name='about'),
    url(r'^past_events$', views.past_events, name='past_events?perPage=100'),
    url(r'^upcoming_events$', views.upcoming_events, name='upcoming_events'),
    url(r'^upcoming_events/(?P<event_id>[0-9]+)/$', views.event_page_base, name='details'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^gallery$', views.gallery_images, name='gallery_images'),
    url(r'^base$', views.base, name='Base')
]
