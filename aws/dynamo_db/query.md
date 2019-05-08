## Querying and Scanning

With the table full of items, you can then query or scan the items in the table using the [`DynamoDB.Table.query()`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.query) or [`DynamoDB.Table.scan()`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.scan) methods respectively. To add conditions to scanning and querying the table, you will need to import the [`boto3.dynamodb.conditions.Key`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/dynamodb.html#boto3.dynamodb.conditions.Key) and[`boto3.dynamodb.conditions.Attr`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/dynamodb.html#boto3.dynamodb.conditions.Attr) classes. The [`boto3.dynamodb.conditions.Key`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/dynamodb.html#boto3.dynamodb.conditions.Key) should be used when the condition is related to the key of the item. The [`boto3.dynamodb.conditions.Attr`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/dynamodb.html#boto3.dynamodb.conditions.Attr) should be used when the condition is related to an attribute of the item:

```
from boto3.dynamodb.conditions import Key, Attr
```

This queries for all of the users whose `username` key equals `johndoe`:

```
response = table.query(
    KeyConditionExpression=Key('username').eq('johndoe')
)
items = response['Items']
print(items)
```

Expected Output:

```
[{u'username': u'johndoe',
  u'first_name': u'John',
  u'last_name': u'Doe',
  u'account_type': u'standard_user',
  u'age': Decimal('25'),
  u'address': {u'city': u'Los Angeles',
               u'state': u'CA',
               u'zipcode': Decimal('90001'),
               u'road': u'1 Jefferson Street'}}]
```

Similarly you can scan the table based on attributes of the items. For example, this scans for all the users whose `age` is less than `27`:

```
response = table.scan(
    FilterExpression=Attr('age').lt(27)
)
items = response['Items']
print(items)
```

Expected Output:

```
[{u'username': u'johndoe',
  u'first_name': u'John',
  u'last_name': u'Doe',
  u'account_type': u'standard_user',
  u'age': Decimal('25'),
  u'address': {u'city': u'Los Angeles',
               u'state': u'CA',
               u'zipcode': Decimal('90001'),
               u'road': u'1 Jefferson Street'}},
 {u'username': u'bobsmith',
  u'first_name': u'Bob',
  u'last_name': u'Smith',
  u'account_type': u'standard_user',
  u'age': Decimal('18'),
  u'address': {u'city': u'Louisville',
               u'state': u'KY',
               u'zipcode': Decimal('40213'),
               u'road': u'3 Madison Lane'}}]
```

You are also able to chain conditions together using the logical operators: `&` (and), `|` (or), and `~` (not). For example, this scans for all users whose `first_name` starts with `J` and whose `account_type` is `super_user`:

```
response = table.scan(
    FilterExpression=Attr('first_name').begins_with('J') & Attr('account_type').eq('super_user')
)
items = response['Items']
print(items)
```

Expected Output:

```
[{u'username': u'janedoering',
  u'first_name': u'Jane',
  u'last_name': u'Doering',
  u'account_type': u'super_user',
  u'age': Decimal('40'),
  u'address': {u'city': u'Seattle',
               u'state': u'WA',
               u'zipcode': Decimal('98109'),
               u'road': u'2 Washington Avenue'}}]
```

You can even scan based on conditions of a nested attribute. For example this scans for all users whose `state` in their `address` is `CA`:

```
response = table.scan(
    FilterExpression=Attr('address.state').eq('CA')
)
items = response['Items']
print(items)
```

Expected Output:

```
[{u'username': u'johndoe',
  u'first_name': u'John',
  u'last_name': u'Doe',
  u'account_type': u'standard_user',
  u'age': Decimal('25'),
  u'address': {u'city': u'Los Angeles',
               u'state': u'CA',
               u'zipcode': Decimal('90001'),
               u'road': u'1 Jefferson Street'}},
 {u'username': u'alicedoe',
  u'first_name': u'Alice',
  u'last_name': u'Doe',
  u'account_type': u'super_user',
  u'age': Decimal('27'),
  u'address': {u'city': u'Los Angeles',
               u'state': u'CA',
               u'zipcode': Decimal('90001'),
               u'road': u'1 Jefferson Street'}}]
```

For more information on the various conditions you can use for queries and scans, refer to [*DynamoDB Conditions*](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/customizations/dynamodb.html#ref-dynamodb-conditions).

## Deleting a Table

Finally, if you want to delete your table call [`DynamoDB.Table.delete()`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Table.delete):

```
table.delete()
```