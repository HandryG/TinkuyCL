import boto3
import pandas as pd
import os

def get_tinkuy_coords_df():
    dynamodb = boto3.client('dynamodb',\
                      aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],\
                      aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'],\
                      region_name = os.environ['AWS_DEFAULT_REGION'])
    response = dynamodb.scan(TableName='tinkuy-coords')
    df = pd.DataFrame.from_dict(response['Items'])
    return df
