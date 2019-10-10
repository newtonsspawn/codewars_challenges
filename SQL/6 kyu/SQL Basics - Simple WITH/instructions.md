# SQL Basics: Simple WITH


## Instructions

For this challenge you need to create a `SELECT` statement, this `SELECT` 
statement will use an `IN` to check whether a department has had a sale with a 
`price` over `90.00` dollars BUT the sql MUST use the `WITH` statement which 
will be used to select all columns from `sales` where the `price` is greater 
than `90.00`. You must call this sub-query `special_sales`.


### Database Schema

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

Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.