import boto3
import pictures_of_the_day
import video_of_the_day
import json

print('Loading function')
s3 = boto3.resource('s3')


def respond(err, origin, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else res, 
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': origin,
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'            
        },
    }


def lambda_handler(event, context):
    print("Received event: " + json.dumps(event, indent=2))
    print(event)

    origin = get_origin(event)

    path = event.get("path")
    if path == "/picturesOfTheDay/data":
        fileString = pictures_of_the_day.get_pictures_of_the_day_data()
        return respond(None, origin, fileString)
    elif path == "/videoOfTheDay/data":
        fileString = video_of_the_day.get_video_of_the_day_data()
        return respond(None, origin, fileString)

# The Access-Control-Allow-Origin header can only return one values.
# We want to support multiple values (localhost, beta, www)
# So check the origin passed in, and if it matches one of those valid
# values then return it.
# Otherwise return an empty string
def get_origin(event):
    origin = ""
    # The event JSON looks like
    # { "multiValueHeaders": { "origin": ["https://beta.marinkofamily.com"] } }
    # "origin" might not always be set, like when calling from Postman
    multiValueHeaders = event.get("multiValueHeaders")
    if multiValueHeaders != None:
        print("multiValueHeaders are found")
        originList = multiValueHeaders.get("origin")
        if originList != None:
            origin = originList[0]
            print("Got origin from event: " + origin)
        else:
            print("origin not in event")

    if origin in ["http://localhost:8080", "https://beta.marinkofamily.com", "https://www.marinkofamily.com"]:
        print("Origin is valid and is: " + origin)
        return origin
    else:
        print("Origin is not valid")
        return ''

    
