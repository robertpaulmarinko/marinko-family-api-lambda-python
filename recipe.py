import boto3
import io

s3 = boto3.resource('s3')

def get_recipes():
    bucket = s3.Bucket('family-web-site-data')
    object = bucket.Object('menu/recipe-box.json')

    # https://docs.python.org/3.6/library/io.html#io.BytesIO
    file_stream = io.BytesIO()
    object.download_fileobj(file_stream)

    fileBytes = file_stream.getvalue()
    # https://docs.python.org/3.6/library/stdtypes.html?highlight=decode#bytes.decode
    fileString = fileBytes.decode('UTF-8')
    print("Recipe file: " + fileString)

    return fileString
