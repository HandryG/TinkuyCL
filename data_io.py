import boto3
import pandas as pd

def get_tinkuy_coords_df():
    dynamodb = boto3.client('dynamodb',\
                      aws_access_key_id='AKIAIN7WLEJ3I6L4JQSQ',\
                      aws_secret_access_key='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',\
                      region_name='us-east-1')
    response = dynamodb.scan(TableName='tinkuy-coords')
    df = pd.DataFrame.from_dict(response['Items'])
    return df
