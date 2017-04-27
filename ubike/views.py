# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:12:45 2017

@author: Edison Song
"""

from django.http import HttpResponse
import ubike.act
# Create your views here.
def index(request):
    if request.method == 'GET':
        lat = request.GET.get('lat', ' ')
        lng = request.GET.get('lng', ' ')
        data = ubike.act.stations.find2(lat, lng)
        posts = list()
        if len(data['result']) == 2:
            posts.append('Content-Type: application/json'+'<br>'+'{'+'<br>'+'&emsp;&emsp;"code" : '+str(data['code'])+','+'<br>'+'&emsp;&emsp;"result" : ['+'<br>'+'&emsp;&emsp;&emsp;&emsp;'+'{"station":'+str(data['result'][0]['station'])+',&ensp;"num_ubike":'+str(data['result'][0]['num_ubike'])+'},'+'<br>'+'&emsp;&emsp;&emsp;&emsp;'+'{"station":'+str(data['result'][1]['station'])+',&ensp;"num_ubike":'+str(data['result'][1]['num_ubike'])+'}'+'<br>'+'&emsp;&emsp;]'+'<br>'+'}')
        else:
            posts.append('Content-Type: application/json'+'<br>'+'{'+'<br>'+'&emsp;&emsp;"code" : '+str(data['code'])+','+'<br>'+'&emsp;&emsp;"result" : []'+'<br>'+'}')
        return HttpResponse(posts)
    else:
        return HttpResponse(status=400)
        



