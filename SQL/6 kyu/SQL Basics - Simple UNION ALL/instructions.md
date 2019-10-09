# SQL Basics: Simple UNION ALL


## Instructions

For this challenge you need to create a `UNION` statement. There are two tables 
`ussales` and `eusales`. The parent company tracks each sale at its respective 
location in each table. You must all filter the sale `price` so it only returns 
rows with a sale greater than `50.00`. You have been tasked with combining that 
data for future analysis. Order by location (US before EU), then by id.


### Schemas

```
(us/eu)sales table schema
- id
- name
- price
- card_name
- card_number
- transaction_date

resultant table schema
- location (EU for eusales and US for ussales)
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