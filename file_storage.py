import boto3
import io
import uuid
import botocore

s3 = boto3.resource('s3')

FAMILY_WEB_SITE_BUCKET = 'family-web-site-data'

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
def create_presigned_upload_url():
    # Generate a presigned URL S3 PUT request URL
    object_name = uuid.uuid4().hex + '.jpg'
    expiration=3600

    # Generate a presigned S3 POST URL
    s3_client = boto3.client('s3', region_name='us-east-2',  endpoint_url='https://s3.us-east-2.amazonaws.com', config=botocore.client.Config(signature_version='s3v4'))
    response = s3_client.generate_presigned_url('put_object',
                                                Params={'Bucket': 'family-web-site-recipe-images',
                                                        'Key': object_name,
                                                        'ContentType':'image/jpeg'},
                                                ExpiresIn=expiration)                                                 
    # The response contains the presigned URL and required fields
    return response    