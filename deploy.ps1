Compress-Archive -Path '*.py' -Update -DestinationPath 'lambda.zip'
aws lambda update-function-code --region us-east-2 --profile default --function-name marinko-family-web-site-python --publish --zip-file fileb://lambda.zip
