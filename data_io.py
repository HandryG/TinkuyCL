import boto3
import pandas as pd
import os
import numpy as np

def get_tinkuy_coords_df():
    dynamodb = boto3.client('dynamodb',\
                      aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],\
                      aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'],\
                      region_name = os.environ['AWS_DEFAULT_REGION'])
    response = dynamodb.scan(TableName='tinkuy-coords')
    df = pd.DataFrame.from_dict(response['Items'])
    return df

def get_tinkuy_coords_np():
    dynamodb = boto3.client('dynamodb',\
                      aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],\
                      aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'],\
                      region_name = os.environ['AWS_DEFAULT_REGION'])
    response = dynamodb.scan(TableName='tinkuy-coords')
    
    points = []
    i = 1
    for item in response['Items']:
        #print(item)
        point = [float(item['latitud']['S']),float(item['longitud']['S'])]
        print(point)
        i += 1
        points.append(points)
        
    return np.array(points)
