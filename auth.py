import json
import boto3
import base64
from botocore.exceptions import ClientError
import uuid
import file_storage

s3 = boto3.resource('s3')

# name of file that contains valid auth token
AUTH_FILE = 'auth-token.txt'

class LoginResponse:
    success = False
    token = ""

# Verifies if the password is valid.
# If it is, returns seccess = true a login token
# If it is not, or the password could not be loaded, returns success = false
# request is a JSON string with one field called "password"
def attempt_login(request):
    requestJson = json.loads(request);
    response = LoginResponse()
    
    password = get_password()
    if password == "":
        print("Could not load the password")
        response.success = False
        response.token = ""
    elif requestJson.get("password") == password:
        print("Password is valid")
        response.success = True
        response.token = generate_and_save_token()
    else:
        print("Password is not valid")
        response.success = False
        response.token = ""
    
    return json.dumps(response.__dict__)

# gets the password from the secret manager
def get_password():

    secret_name = "marinko_family_website_password"
    region_name = "us-east-2"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
            # See https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
            # for information about exceptions
            print("Error getting password from secret manager")
            print(e.response['Error']['Code'])
            secret = ""
    else:
        # Decrypts secret using the associated KMS CMK.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            print("Expected password to be a string, but got a binary instead")
            secret = ""
            
            
    return secret

def generate_and_save_token():
    token =  uuid.uuid4()
    
    s3.Object(file_storage.FAMILY_WEB_SITE_BUCKET, AUTH_FILE).put(Body=token.hex)

    return token.hex;


def is_token_valid(check_token)    :
    valid_token = file_storage.get_file(file_storage.FAMILY_WEB_SITE_BUCKET, AUTH_FILE)
    return valid_token == check_token