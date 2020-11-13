import json
import boto3
import random
import os
import math
#from shapely.geometry import Point

usr_index = 241 

def generate_random(lat ,lon, r):
    R    = 6378.1 #Radius of the Earth
    brng = random.uniform(0,2*math.pi) #Random degrees converted into to radians.
    d    = random.uniform(0,r) #Random distance in km

    lat1 = math.radians(lat) #Current lat point converted to radians
    lon1 = math.radians(lon) #Current long point converted to radians

    lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
    math.cos(lat1)*math.sin(d/R)*math.cos(brng))

    lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),math.cos(d/R)-math.sin(lat1)*math.sin(lat2))
    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)
    #pnt  = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))

    return [lat2, lon2]

def load_locations(n, lat, lon, r, dynamodb=None):

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',\
                      aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],\
                      aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'],\
                      region_name = os.environ['AWS_DEFAULT_REGION'])
                      
        #dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('tinkuy-coords-qas')
    
    global usr_index

    ini = usr_index
    fin = usr_index + n - 1
    usr_index = fin + 1

    for i in range(ini,fin):
        _point = generate_random(lat, lon, r)
        location_dict = {}
        location_dict['usr_tlg']  = "#TEST_"   + str(i)
        location_dict['tstamp']   = 1605151084 + random.randint(0,86400)
        location_dict['latitud']  = str(_point[0])
        location_dict['longitud'] = str(_point[1])
        location_dict['status']   = "normal"
        print(location_dict)
        location_json = json.dumps(location_dict)
        table.put_item(Item=location_dict)


if __name__ == '__main__':
    
    #load_locations(30,-12.131819,-77.030297, 1)#Larcomar
    #load_locations(30,-12.046452,-77.042785, 1)#Plaza 2 de Mayo
    #load_locations(10,60,-12.051806,-77.034629)#Plaza San Martin
    load_locations(150,-12.054520,-77.030175, 0.05)#Av. Abancay
    load_locations(100,-12.048730,-77.039021, 0.1)#Av. Tacna
    load_locations(30,-12.077013,-77.082974, 0.2)#Plaza San Miguel
    #load_locations(30,-12.054629,-77.030219, 0.5)#Nicolas de Pierola tramo 1
    #load_locations(30,-12.053787,-77.031476, 0.5)#Nicolas de Pierola tramo 2
    #load_locations(30,-12.052077,-77.034069, 0.5)#Nicolas de Pierola tramo 4
