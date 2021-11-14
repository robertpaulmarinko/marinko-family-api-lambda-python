import boto3
import io
import uuid
import botocore
import json

s3 = boto3.resource('s3')

FAMILY_WEB_SITE_BUCKET = 'family-web-site-data'
FAMILY_WEB_SITE_RECIPE_IMAGES = 'family-web-site-recipe-images'

def get_file(bucket, file_key):
    bucket = s3.Bucket(bucket)
    object = bucket.Object(file_key)

    # https://docs.python.org/3.6/library/io.html#io.BytesIO
    file_stream = io.BytesIO()
    object.download_fileobj(file_stream)

    fileBytes = file_stream.getvalue()
    # https://docs.python.org/3.6/library/stdtypes.html?highlight=decode#bytes.decode
    fileString = fileBytes.decode('UTF-8')

    return fileString

def put_file(bucket, file_key, file):
    s3.Object(bucket, file_key).put(Body=file)

# Generate a presigned URL S3 PUT request URL
def create_presigned_upload_url(bucket, file_key, expiration, content_type ):
    # Note that setting the region, endpoint and signature_version are all required to construct
    # a URL that will work.  See readme.md file for more information.
    s3_client = boto3.client('s3', region_name='us-east-2',  endpoint_url='https://s3.us-east-2.amazonaws.com', config=botocore.client.Config(signature_version='s3v4'))
    url = s3_client.generate_presigned_url('put_object',
                                                Params={'Bucket': bucket,
                                                        'Key': file_key,
                                                        'ContentType':content_type},
                                                ExpiresIn=expiration)                                                 
    return url