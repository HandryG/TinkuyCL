import boto3
import os
import time
from the_clustering import do_clustering

medoid_list = {}
medoid_list['list']=[]

point_list = do_clustering(3,10)
medoid_list['tstamp'] = time.time() 
medoid_list['points'] = point_list
medoid_list['id'] = 1
print(medoid_list)

dynamodb = boto3.resource('dynamodb',\
                      aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],\
                      aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'],\
                      region_name = os.environ['AWS_DEFAULT_REGION'])
                  
table = dynamodb.Table('tinkuy-clusters')
#table.delete_item(Key={'id': id})
table.put_item(medoid_list)
  
