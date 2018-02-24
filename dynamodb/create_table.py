import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Create the DynamoDB table.
table = dynamodb.create_table(
    TableName='runs',
    KeySchema=[
        {
            'AttributeName': 'run_accession',
            'KeyType': 'HASH'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'run_accession',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 25,
        'WriteCapacityUnits': 25
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='runs')

# Print out some data about the table.
print(table.item_count)
