from datetime import datetime
from urllib import urlencode
from urllib2 import urlopen
from StringIO import StringIO
from numpy import genfromtxt
import ast
import re

stations_url_str = 'http://data.hisparc.nl/api/stations'
stations_url = urlopen(stations_url_str)
stations = stations_url.read()

# can't just look for numbers as some names have numbers in
# so look for "number: number"
numbers = re.findall(r'"number": \d+', stations)
station_ids = []
for num in numbers:
        station_ids.append(int(re.findall(r'\d+', num)[0]))

print "Found these station ids"
print station_ids

base_url = "http://data.hisparc.nl/api/station/%d/"

for id in station_ids:
	url = urlopen(base_url % (id))
	meta_data = ast.literal_eval(url.read())
	print( type( meta_data ) )
	print( meta_data )
