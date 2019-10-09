# SQL Basics: Top 10 Customers by Total Payments Amount


## Instructions


### Overview

For this kata we will be using the DVD Rental database.

Your are working for a company that wants to reward its top 10 customers with a 
free gift. You have been asked to generate a simple report that returns the top 
10 customers by total amount spent. Total number of payments has also been 
requested.


### Task

The query should output the following columns:
- customer_id [int4]
- email [varchar]
- payments_count [int]
- total_amount [float]

and has the following requirements:
- only returns the 10 top customers
- ordered by total amount spent


### Database Schema

```
customer
- customer_id
- store_id
- first_name
- last_name
- email
- address_id
- activebool
- create_date
- last_update
- active

payment
- payment_id
- customer_id
- staff_id
- rental_id
- amount
- payment_date
```

![](http://www.postgresqltutorial.com/wp-content/uploads/2018/03/dvd-rental-sample-database-diagram.png)