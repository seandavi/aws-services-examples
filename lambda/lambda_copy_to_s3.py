import urllib.request
import xml.etree.ElementTree as etree
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    bucket = event['bucket']
    key    = event['key']
    url    = event['url']
    with urllib.request.urlopen(url) as response:
        object = s3.Object(bucket, key)
        object.put(Body = response.read())
        return { "message": "OK" }
