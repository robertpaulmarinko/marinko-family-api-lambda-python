# Marinko Family Website API

This it the API written in Python, running in an AWS Lambda, and exposed to the web using AWS API Gateway.


'
## API Gateway Setup

Create the `marinko-family-web-site-python` lambda and during the creation process requested that an API Gateway be created.

When first tried to use the API Gateway via postman, got this error: `Missing Authentication Token`

Problem was that AWS added the resource as `marinko-family-web-site-python`, so this URL works:

`https://p89uuc2375.execute-api.us-east-2.amazonaws.com/default/marinko-family-web-site-python`

Manually created my own Method at the root, to make this URL work:

`https://p89uuc2375.execute-api.us-east-2.amazonaws.com/default`


Then manually created a `Proxy` resource so that the API would take any incoming request, such as

`https://p89uuc2375.execute-api.us-east-2.amazonaws.com/default/pictures`


## AWS SDK

Boto3

https://boto3.amazonaws.com/v1/documentation/api/latest/index.html


## Deploy

To deploy to AWS, run 

`./deploy.ps1`

This is a PowerShell scripts that zips up the source files and uploads to the lambda

https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.archive/compress-archive?view=powershell-7.1

## Testing

Run a test file like  this

`py test-get-video-of-the-day.py`


## Issues

### CORS

Only only website can be returned in the Access-Control-Allow-Origin header.  So had to write a function to check the incoming origin, and if it was valid, return it.

## Password storage
Created a KMS key called `marinko_family_website_password_key`

Created a Secret called `marinko_family_website_password`

Updated `marinko-family-web-site` role to allow decoding using KMS key and reading of secret.

## Reading a JSON array and editing the content

Reading the array

https://stackoverflow.com/questions/47060035/python-parse-json-array

https://pythonexamples.org/python-json-to-list/

looping through an array while also getting the index

https://treyhunner.com/2016/04/how-to-loop-with-indexes-in-python/

## File Upload

Use pre-signed URL's to upload directly to S3

[AWS Documentation for Pre-signed Upload URL](https://aws.amazon.com/blogs/compute/uploading-to-amazon-s3-directly-from-a-web-or-mobile-application/)

[Boto3 Example for creating Pre-Signed Upload URL](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-presigned-urls.html)

[Boto3 Function Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.generate_presigned_url)

[Trouble shooting security issues](https://aws.amazon.com/premiumsupport/knowledge-center/s3-troubleshoot-403/)

Made a new bucket called family-web-site-recipe-images that did nto block public access.

Started getting a timeout error message.  According to AWS its because the Content-Length is not correct. although Postman should be setting that.  https://aws.amazon.com/premiumsupport/knowledge-center/s3-socket-connection-timeout-error/

Stopped Postman from sending Content-Length and it got farther

Got this error

The authorization mechanism you have provided is not supported. Please use AWS4-HMAC-SHA256.

Added this code as suggested [here](https://stackoverflow.com/questions/27400105/using-boto-for-aws-s3-buckets-for-signature-v4)

```python
s3_client = boto3.client('s3', region_name='us-east-2')
```

Then got a "SignatureDoesNotMatch" error

Also specified the region URL as talked about [here](https://github.com/boto/boto3/issues/1149)

```python
s3_client = boto3.client('s3', region_name='us-east-2',  endpoint_url='https://s3.us-east-2.amazonaws.com', config=botocore.client.Config(signature_version='s3v4'))
```
Then had to put "back" the Content-Length header that I talked about removing above.