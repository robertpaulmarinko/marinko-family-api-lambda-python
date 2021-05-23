# Marinko Family Website API

This it the API written in Python, running in an AWS Lambda, and exposed to the web using AWS API Gateway.



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
