from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
import json
import ubike.act
#-*- coding:utf-8 -*-
# Create your views here.
def index(request):
    if request.method == 'GET':
        template = get_template('index.html')
        lat = request.GET.get('lat', ' ')
        lng = request.GET.get('lng', ' ')
        try:
            float(lat)
            float(lng)
            data = ubike.act.stations.find2(lat, lng)
            posts = {}
            if len(data['result']) == 2:
                posts['Content-Type'] = 'application/json'
                posts['code'] = data['code']
                posts['result'] = [{"station": data['result'][0]['station'], 'num_ubike': data['result'][0]['num_ubike']}, {"station": str(data['result'][1]['station']), 'num_ubike': data['result'][1]['num_ubike']}]
            else:
                posts['Content-Type'] = 'application/json'
                posts['code'] = data['code']
                posts['result'] = []
            return HttpResponse(json.dumps(posts, ensure_ascii=False))
        except:
            html = template.render(locals())
            return HttpResponse(html)
    else:
        return HttpResponse(status=400)