import random
from shapely.geometry import Point

def generate_random():
    _point = []
    minx = -12.0494294
    miny = -77.0366168
    maxx = -12.0548508
    maxy = -77.0304093

    pnt = Point(random.uniform(minx, maxx), random.uniform(miny, maxy))
    return pnt

def load_locations(n, dynamodb=None):

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb',aws_access_key_id='AKIAIN7WLEJ3I6L4JQSQ', aws_secret_access_key='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', region_name='us-east-1')
        #dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('tinkuy-coords')

    for i in range(n):
        _point = generate_random()
        location_dict = {}
        location_dict['usr_tlg']  = "#TEST_"   + str(i)
        location_dict['tstamp']   = 1605151084 + random.randint(0,86400)
        location_dict['latitud']  = str(_point.x)
        location_dict['longitud'] = str(_point.y)
        print(location_dict)
        location_json = json.dumps(location_dict)
        table.put_item(Item=location_dict)


if __name__ == '__main__':

    load_locations(500)
