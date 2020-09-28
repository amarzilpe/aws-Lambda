#when a json file is uploaded in the s3 bucket Lambda function get call and 
#function will create a table in DynamoDB 
import boto3
import json
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    bucket = event['Record'][0]['s2']['bucket']['name']
    json_file_name = event['Record'][0]['s3']['object']['key']
    json_object = s3_client.get_object(Bucket=bucket,key=json_file_name)
    jsonFileReader=json_object['Body'].read()
    jsonDict=json.loads(jsonFileReader)
    table=dynamodb.Table('employees')
    table.put_item(Item=jsonDict)
    return "hey completed successfully"