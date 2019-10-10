# SQL Basics: Simple JOIN and RANK


## Instructions

For this challenge you need to create a simple `SELECT` statement that will 
return all columns from the `people` table, and `join` to the `sales` table so 
that you can return the `COUNT` of all sales and `RANK` each person by their 
`sale_count`.


### Database Schema

```
people table schema
- id
- name

sales table schema
- id
- people_id
- sale
- price
```


### Task

You should return all people fields as well as the `sale` count as 
`"sale_count"` and the `rank` as `"sale_rank"`.


### Note

Your solution should use pure SQL. Ruby is used within the test cases to do the 
actual testing.