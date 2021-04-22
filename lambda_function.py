import boto3
import pictures_of_the_day
import json

print('Loading function')
s3 = boto3.resource('s3')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else res, 
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': 'http://localhost:8080',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'            
        },
    }


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    path = event.get("path")
    if path == "/picturesOfTheDay/data":
        fileString = pictures_of_the_day.get_pictures_of_the_day_data()
        return respond(None, fileString)
