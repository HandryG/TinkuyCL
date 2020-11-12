import boto3
import os
import time
from the_clustering import do_clustering

medoid_list = {}

points = do_clustering(3,10)
points_list = []
for point in points:
  point_dict = {}
  point_dict['SS'] = [str(coord) for coord in point]
  points_list.append(point_dict)

medoid_list['tstamp'] = {'S':str(time.time()) }
medoid_list['points'] = {'L':points_list }
medoid_list['cluster_id'] = {'S':'0'}

print('\nItem for DynamoDB:\n',medoid_list)

dynamodb = boto3.resource('dynamodb',\
                      aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],\
                      aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'],\
                      region_name = os.environ['AWS_DEFAULT_REGION'])
                  
try:
  #dynamodb.delete_item(Key={'id': id})
  #dynamodb.update_item(TableName='tinkuy-clusters',Item=medoid_list)
  table = dynamodb.Table('tinkuy-clusters')
  response = table.update_item(
        Key={
            'cluster_id': medoid_list['cluster_id']
        },
        UpdateExpression="set tstamp=:s, points=:p",
        ExpressionAttributeValues={
            ':t': medoid_list['tstamp'],
            ':p': medoid_list['points']
        },
        ReturnValues="UPDATED_NEW"
    )
  print("Medoids updated in dynamo")
except:
  print("Medoid update failed")
 
