# Dealing With Messy Data


## Instructions

Your company has an internal policy to determine your customers' credit
limit, but this procedure has been questioned recently by the board as
being too conservative.

Your CEO wants to increase the current customer base credit limits in
order to upsell a new line of products. In order to do that, the
company hired several external consultancies to produce new credit
limit estimates.

The problem is that each agency has produced the report in its own
format. Some use the format `"First-name Last-name"` to identify a
person, others use the format `"Last-name, First-name"`. There is also
no consensus on how to capitalize each word, so some used all
uppercase, others used all lowercase, and some used mixed-case.


### Table Schemas

Internally, the data is structured as follows:

```
customers Table Schema
- id: INT
- first_name: TEXT
- last_name: TEXT
- credit_limit: FLOAT
```

The data you've received from all agencies was consolidated in the following table:

```
prospects Table Schema
- full_name: TEXT
- credit_limit: FLOAT
```

Keep in mind that the agencies had access only to a partial customer
base. There is also the possibility of more than one agency prospecting
the same customer, so it's highly likely that there will be duplicates.
Finally, they've prospected customers that were not in your customer
base as well.

For this task you are interested in the prospected customers that are
already in your customer base and the prospected credit limit if it is
higher than your internal estimate. When more than one agency
prospected the same customer, chose the highest estimate.

```
output Table Schema
- first_name
- last_name
- old_limit [the current credit_limit]
- new_limit [the highest credit_limit found]
```


### Notes

Only list the customers that a higher credit limit was found.