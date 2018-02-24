# DynamoDB 

This follows the examples in
the
[boto3 DynamoDB documentation](http://boto3.readthedocs.io/en/latest/guide/dynamodb.html). The
data are simple json records from the NCBI SRA database. A single key
is used here, just to illustrate the technical aspects of creating,
inserting, and fetching a single record.

- Example json data `sra_experiment_test.json.gz`

## To use:

Run the following

1. `create_table.py`: run once 
2. `put_one_item.py`: puts a single item
3. `batch_put_items.py`: creates and utilizes a batch table operation

**Note**: DynamoDB does not allow floats, only Decimal
(`decimal.Decimal`). The incantation for the json library is:

```python
json.loads(StringData, parse_float = decimal.Decimal)
```


