# DynamoDB 

This follows the examples in the [boto3 DynamoDB documentation](http://boto3.readthedocs.io/en/latest/guide/dynamodb.html).

- Example json data `sra_experiment_test.json.gz`
- `create_table.py`: run once 
- `put_one_item.py`: puts a single item
- `batch_put_items.py`: creates and utilizes a batch table operation

**Note**: DynamoDB does not allow floats, only Decimal
(`decimal.Decimal`). The incantation for the json library is:

```python
json.loads(StringData, parse_float = decimal.Decimal)
```


