# SQL Basics: Simple EXISTS


## Instructions

For this challenge you need to create a `SELECT` statement, this `SELECT` 
statement will use an `EXISTS` to check whether a department has had a sale 
with a `price` over `98.00` dollars.


### Schemas

```
departments table schema
- id
- name

sales table schema
- id
- department_id (department foreign key)
- name
- price
- card_name
- card_number
- transaction_date

resultant table schema
- id
- name
```


### Note

Your solution should use pure SQL. Ruby is used within the test cases to do the 
actual testing.

**DO NOT** alias tables as this can cause a failure.