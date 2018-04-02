# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 02:19:59 2017

@author: Edison Song
"""

import requests
#from math import radians, cos, sin, asin, sqrt

class data_import():        
    def ub_load():
        youbike_api = 'http://data.taipei/youbike'
        response = requests.get(youbike_api)
        data = response.json()
        if data['retCode'] == 1:
            youbike={}
            for key, value in data['retVal'].items():
                #longitude
                longitude = value['lng']
                #latitude
                latitude = value['lat']
                #numbers of ubike can borrow
                num_ubike = value['sbi']
                #station name
                station = value['sna']
                #station name in English
                station_en = value['snaen']
                #number of ubike can retrun
                num_vacancies = value['bemp']
                #the station state
                state = value['act']
                # station id as key
                youbike[value['sno']] = {'lng' : longitude, 'lat' : latitude,\
                                         'sbi' : num_ubike, 'sna' : station,\
                                         'snaen' : station_en, 'bemp' : num_vacancies,\
                                         'act' : state}
             
            return youbike
        else:
            return False

class condition(object):
    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng
    def is_valid(self):  
        try:
            lat = float(self.lat)
            lng = float(self.lng)
            if -90 <= lat <= 90 and -180 <= lng <= 180:
                return True
            else:
                return False
        except ValueError:
            return False

    def is_in_boundary(self):
        # get located point
        response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lng}'.format(lat=self.lat, lng=self.lng))
        data = response.json()
        if data['status'] == 'OK':
            if len(data['results'][0]['address_components'])>=3:
                city = data['results'][0]['address_components'][-3]['short_name']

                if city == 'Taipei City':
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def are_stations_full(self, data):  
        for i in data:
            if int(data[i]['bemp']) > 0:
                return False
        return True
    
    def is_active(self, data):
        for i in data:
            if int(data[i]['act']) == 1:
                return True
            else:
                return False
                
class stations():

#    def haversine(lat1, lng1, latp, lngp):
#        # convert decimal degrees to radians 
#        lat1, lng1, latp, lngp = map(radians, [lat1, lng1, latp, lngp])
#        # haversine formula 
#        dlon = lngp - lng1 
#        dlat = latp - lat1 
#        a = sin(dlat/2)**2 + cos(lat1) * cos(latp) * sin(dlon/2)**2
#        c = 2 * asin(sqrt(a)) 
#        return c

    def distance(lat1, lng1, latp, lngp):
        #take latitude and longitude as x and y coordinate in x-y plane
        d = (lat1-latp)**2+(lng1-lngp)**2
        return d
            
    def find2(lat, lng):
            
        if not condition(lat, lng).is_valid():
            data = {'code' : -1, 'result' : []}
            return data
            
        if not condition(lat, lng).is_in_boundary():
            data = {'code' : -2, 'result' : []}
            return data
                
        youbike = data_import.ub_load()
        if not youbike:
            data = {'code' : -3, 'result' : []}
            return data
                
        if condition(lat, lng).are_stations_full(youbike):
            data = {'code' : 1, 'result' : []}
            return data
                        
        lngp, latp = float(lng), float(lat)
        dis = []
        for key, value in youbike.items():
            dis.append([stations.distance(float(value['lat']), float(value['lng']), latp, lngp), key])
        dis.sort()
        station = []
        for entry in dis:
            if len(station) == 2:
                break
            sno = entry[1]
            num_ubike = int(youbike[str(sno)]['sbi'])
            if num_ubike > 0:
                if int(youbike[str(sno)]['act']) == 1:
                    station_entry = { 'station': u"%s" %youbike[str(sno)]['sna'], 'num_ubike': str(num_ubike) }
                    station.append(station_entry)
        data = { 'code' : 0, 'result' : station }
        return data
