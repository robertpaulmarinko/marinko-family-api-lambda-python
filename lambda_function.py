import boto3
import pictures_of_the_day
import json

print('Loading function')
s3 = boto3.resource('s3')


def respond(err, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else json.dumps(res),
        'headers': {
            'Content-Type': 'application/json',
        },
    }


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    path = event.get("path")
    if path == "/picturesOfTheDay/data":
        fileString = pictures_of_the_day.get_pictures_of_the_day_data()
        return respond(None, fileString)
