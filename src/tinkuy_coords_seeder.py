import json
import boto3
import random
import os
from shapely.geometry import Point

def generate_random(minx ,miny):
    _point = []
    maxx = minx + 0.005
    maxy = miny + 0.005

    pnt = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
    return pnt

def load_locations(ini,fin, minx, miny, dynamodb=None):

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',\
                      aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],\
                      aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'],\
                      region_name = os.environ['AWS_DEFAULT_REGION'])
                      
        #dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('tinkuy-coords-qas')

    for i in range(ini,fin):
        _point = generate_random(minx, miny)
        location_dict = {}
        location_dict['usr_tlg']  = "#TEST_"   + str(i)
        location_dict['tstamp']   = 1605151084 + random.randint(0,86400)
        location_dict['latitud']  = str(_point.x)
        location_dict['longitud'] = str(_point.y)
        location_dict['status']   = "normal"
        print(location_dict)
        location_json = json.dumps(location_dict)
        table.put_item(Item=location_dict)


if __name__ == '__main__':
    load_locations(  1,150,-12.131819,-77.030297)#Larcomar
    load_locations(10,30,-12.046452,-77.042785)#Plaza 2 de Mayo
    load_locations(10,60,-12.051806,-77.034629)#Plaza San Martin
    load_locations(10,50,-12.054520,-77.030175)#Av. Abancay
    load_locations(10,75,-12.048730,-77.039021)#Av. Tacna
    load_locations(25,75,-12.077013,-77.082974)#Plaza San Miguel
    load_locations(1,30,-12.054629,-77.030219)#Nicolas de Pierola tramo 1
    load_locations(1,30,-12.053787,-77.031476)#Nicolas de Pierola tramo 2
    load_locations(1,30,-12.052704,-77.033051)#Nicolas de Pierola tramo 3
    load_locations(1,30,-12.052077,-77.034069)#Nicolas de Pierola tramo 4
