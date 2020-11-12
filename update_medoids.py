import boto3
import os
import time
from the_clustering import do_clustering

medoid_list = {}
medoid_list['list']=[]

point_list = do_clustering(3,10)
medoid_list['tstamp'] = {'N':time.time() }
medoid_list['points'] = {'M':point_list  }
print(medoid_list)

dynamodb = boto3.client('dynamodb',\
                      aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],\
                      aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY'],\
                      region_name = os.environ['AWS_DEFAULT_REGION'])
                  
#table = dynamodb.Table('tinkuy-clusters')
#table.delete_item(Key={'id': id})
dynamodb.put_item(TableName='tinkuy-clusters',Item=medoid_list)
  
