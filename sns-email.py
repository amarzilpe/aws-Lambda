import boto3
client = boto3.client('sns')

def lambda_handler(event, context):
    topic_arn = 'arn:aws:sns:us-east-2:422740763249:Prod-server-stop'
    message = 'Hey! The production web server is down'
    client.publish(TopicArn=topic_arn, Message=message)