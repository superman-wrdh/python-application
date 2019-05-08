

# Creating a New Table

## Get the service resource.


## Create the DynamoDB table.
```python

import boto3
dynamodb = boto3.resource('dynamodb')
table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'username',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'last_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'last_name',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)
```
## Wait until the table exists.
    table.meta.client.get_waiter('table_exists').wait(TableName='users')

## Print out some data about the table.
    print(table.item_count)
## Expected Output:

## 0
    This creates a table named users that respectively has the hash and range primary keys username and last_name.
    This method will return a DynamoDB.Table resource to call additional methods on the created table.
   
    
    
# Using an Existing Table
    It is also possible to create a DynamoDB.Table resource from an existing table:
    
 ```python
import boto3

# Get the service resource.
dynamodb = boto3.resource('dynamodb')

# Instantiate a table resource object without actually
# creating a DynamoDB table. Note that the attributes of this table
# are lazy-loaded: a request is not made nor are the attribute
# values populated until the attributes
# on the table resource are accessed or its load() method is called.
table = dynamodb.Table('users')

# Print out some data about the table.
# This will cause a request to be made to DynamoDB and its attribute
# values will be set based on the response.
print(table.creation_date_time)
```
    Expected Output (Please note that the actual times will probably not match up)
    
# Creating a New Item
    Once you have a DynamoDB.Table resource you can add new items to the table using DynamoDB.Table.put_item():
 
 ```python
table.put_item(
   Item={
        'username': 'janedoe',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'age': 25,
        'account_type': 'standard_user',
    }
)
```   

## Getting an Item
## You can then retrieve the object using DynamoDB.Table.get_item():
```python
response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
item = response['Item']
print(item)
```
    Expected Output:
    
    {u'username': u'janedoe',
     u'first_name': u'Jane',
     u'last_name': u'Doe',
     u'account_type': u'standard_user',
     u'age': Decimal('25')}
     
## Updating Item
## You can then update attributes of the item in the table:
```python
table.update_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    },
    UpdateExpression='SET age = :val1',
    ExpressionAttributeValues={
        ':val1': 26
    }
)
```
## Then if you retrieve the item again, it will be updated appropriately:

```python

response = table.get_item(
    Key={
        'username': 'janedoe',
        'last_name': 'Doe'
    }
)
item = response['Item']
print(item)

```
## Expected Output:
    {u'username': u'janedoe',
     u'first_name': u'Jane',
     u'last_name': u'Doe',
     u'account_type': u'standard_user',
     u'age': Decimal('26')}
     
## Deleting Item
## You can also delete the item using DynamoDB.Table.delete_item():

    table.delete_item(
        Key={
            'username': 'janedoe',
            'last_name': 'Doe'
        }
    )


