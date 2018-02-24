#!/bin/bash
aws lambda update-function-code \
    --function-name UrlCopy \
    --zip-file fileb://lambda_copy_to_s3.zip 
