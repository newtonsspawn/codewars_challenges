# SQL Basics: Simple NULL handling


## Instructions

For this challenge you need to create a SELECT statement. This select statement 
must have NULL handling, using COALESCE and NULLIF.

If no `name` is specified you must replace with `[product name not found]`.

If no `card_name` is specified you must replace with `[card name not found]`.

If no `price` is specified you must throw away the record, you must also filter 
the dataset by prices greater than 50.


### Database Schema

```
eusales table schema
- id
- name
- price
- card_name
- card_number
- transaction_date

resultant table schema
- id
- name
- price (greater than 50.00)
- card_name
- card_number
- transaction_date
```


### Note

Your solution should use pure SQL. Ruby is used within the test cases to do the 
actual testing.