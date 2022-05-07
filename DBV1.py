import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')

table = dynamodb.create_table (
    TableName = 'GraphGeneratorTest1',
       KeySchema = [
           {
               'AttributeName': 'ReqId',
               'KeyType': 'HASH'
           },
           {
               'AttributeName': 'userName',
               'KeyType': 'RANGE'
           }
           ],
           AttributeDefinitions = [
               {
                   'AttributeName': 'ReqId',
                   'AttributeType': 'S'
               },
               {
                   'AttributeName':'userName',
                   'AttributeType': 'S'
               }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits':1,
                'WriteCapacityUnits':1
            }
          
    )
print(table)