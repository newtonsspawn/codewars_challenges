# SQL Basics: Simple Table Totaling


## Instructions

For this challenge you need to create a simple query to display each unique 
clan with their total points and ranked by their total points.


### Database Schema

```
people table schema
- name
- points
- clan
```


### Task

- You should then return a table that resembles below:

```
select on
- rank
- clan
- total_points
- total_people
```

- The query must rank each clan by their `total_points`.
- You must return each unqiue clan and if there is no clan name you must 
replace it with `[no clan specified]`.
- You must sum the `total_points` for each clan and the `total_people` within 
that clan.


### Note 

The data is loaded from the live leader board, this means values will change 
but also could cause the kata to time out retrieving the information.

You're solution should use pure SQL. Ruby is used within the test cases to do 
the actual testing.