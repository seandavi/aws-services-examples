#!/bin/bash
aws lambda create-function \
    --region us-east-1 \
    --function-name UrlCopy \
    --zip-file fileb://lambda_copy_to_s3.zip \
    --role arn:aws:iam::377200973048:role/lambda_s3_exec_role  \
    --handler lambda_copy_to_s3.lambda_handler \
    --runtime python3.6 \
    --timeout 10 \
    --memory-size 128
