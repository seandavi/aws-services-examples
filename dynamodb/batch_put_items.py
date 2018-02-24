import boto3
import gzip
import json

# DynamoDB does not store floats, only decimals
import decimal

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('runs')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
print(table.creation_date_time)

with table.batch_writer(overwrite_by_pkeys=['run_accession']) as batch:
    with gzip.GzipFile('sra_experiment_test.json.gz') as jsonlines:
        for line in jsonlines:
            # DynamoDB does not store floats, only decimals
            entry = json.loads(line.decode(), parse_float=decimal.Decimal)
            batch.put_item(Item = entry)

