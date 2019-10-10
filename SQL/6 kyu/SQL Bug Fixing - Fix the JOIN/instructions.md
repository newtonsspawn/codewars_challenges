# SQL Bug Fixing: Fix the JOIN


## Instructions

Oh no! Timmys been moved into the database division of his software company but 
as we know Timmy loves making mistakes. Help Timmy keep his job by fixing his 
query...

Timmy works for a statistical analysis company and has been given a task of 
calculating the highest average salary for a given job. The sample is compiled 
of 100 applicants each with a job and a salary. Timmy must display each unique 
job, the total average salary, the total people, and the total salary, and 
order by highest average salary. Timmy has some bugs in his query. Help Timmy 
fix his query so he can keep his job!


### Database Schema

```
people table schema
- id
- name

job table schema
- id
- people_id
- job_title
- salary

resultant table schema
- job_title (unique)
- average_salary (float, 2 dp)
- total_people (int)
- total_salary (float, 2 dp)
```


### Note 

Your solution should use pure SQL. Ruby is used within the test cases to do 
the actual testing.