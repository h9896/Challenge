# Challenge
a HTTP API to find 2 nearest ubike station based on latitude and longitude in request parameters.

ex: url = 'https://baekend-test.herokuapp.com//v1/ubike-station/taipei?lat=25.034153&lng=121.568509'

code state:
	1: all ubike stations are full
	0: OK
	-1: invalid latitude or longitude
	-2: given location not in Taipei City
	-3: system error
