import boto3
import pictures_of_the_day
import video_of_the_day
import recipe
import json
import auth

print('Loading function')
s3 = boto3.resource('s3')


def lambda_handler(event, context):
    # Format of event: https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html
    print("Received event: " + json.dumps(event, indent=2))
    print(event)

    origin = get_origin(event)
    if is_request_authorized(event) == False:
        return respond_unauthorized(origin)

    path = event.get("path")
    if path == "/picturesOfTheDay/data":
        fileString = pictures_of_the_day.get_pictures_of_the_day_data()
        return respond(None, origin, fileString)
    elif path == "/videoOfTheDay/data":
        fileString = video_of_the_day.get_video_of_the_day_data()
        return respond(None, origin, fileString)
    elif path == "/recipes":
        fileString = recipe.get_recipes()
        return respond(None, origin, fileString)
    elif path == "/login":
        fileString = auth.attempt_login(event.get("body"))
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

    
def is_request_authorized(event):
    path_does_not_require_auth = [ "/picturesOfTheDay/data", "/videoOfTheDay/data", "/login"  ]
    path = event.get("path")
    if path in path_does_not_require_auth:
        # do auth token required
        print("no auth token is required")
        return True
    else:
        print("auth token is required")
        user_auth_token = get_auth_token_from_header(event)
        print("passed auth token: " + user_auth_token)
        return auth.is_token_valid(user_auth_token)

def get_auth_token_from_header(event)        :
    auth_token = ""
    headers = event.get("headers")
    if headers != None:
        auth_token = headers.get("x-auth-token")
        if auth_token != None:
            return auth_token

    return ""

def respond(err, origin, res=None):
    return {
        'statusCode': '400' if err else '200',
        'body': err.message if err else res, 
        'headers': response_headers(origin)
    }

def respond_unauthorized(origin):
    return {
        'statusCode': '401',
        'headers': response_headers(origin)
    }

def response_headers(origin):
    return {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': origin,
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'            
        }

