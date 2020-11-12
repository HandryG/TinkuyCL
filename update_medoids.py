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
medoid_list['cluster_id'] = {'S':'activo'}

print('\nItem for DynamoDB:\n',medoid_list)

dynamodb_rs = boto3.resource('dynamodb',\
                      aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],\
                      aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'],\
                      region_name = os.environ['AWS_DEFAULT_REGION'])

dynamodb_cl = boto3.client('dynamodb',\
                      aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],\
                      aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'],\
                      region_name = os.environ['AWS_DEFAULT_REGION'])             
#try:
  table = dynamodb_rs.Table('tinkuy-clusters')
  response = table.delete_item(Key={'cluster_id': {'S':'activo'}})
  dynamodb_cl.put_item(TableName='tinkuy-clusters',Item=medoid_list)
  
  print("Medoids updated in dynamo",response )
#except:
  #print("Medoid update failed")
 
