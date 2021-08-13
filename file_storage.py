import boto3
import io

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