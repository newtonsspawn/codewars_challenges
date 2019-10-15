# Relational Division: Find All Movies Two Actors Cast in Together


## Instructions

Given `film_actor` and `film` tables from the
[DVD Rental](http://www.postgresqltutorial.com/postgresql-sample-database/)
sample database find all movies both Sidney Crowe (`actor_id = 105`)
and Salma Nolte (`actor_id = 122`) cast in together and order the
result set alphabetically.


### Table Schema

```
film table schema

 Column     | Type                        | Modifiers
------------+-----------------------------+----------
title       | character varying(255)      | not null
film_id     | smallint                    | not null
```
```
film_actor table schema

 Column     | Type                        | Modifiers
------------+-----------------------------+----------
actor_id    | smallint                    | not null
film_id     | smallint                    | not null
last_update | timestamp without time zone | not null
```
```
actor table schema

 Column     | Type                        | Modifiers
------------+-----------------------------+----------
actor_id    | integer                     | not null
first_name  | character varying(45)       | not null
last_name   | character varying(45)       | not null
last_update | timestamp without time zone | not null'
```
```
output table schema:

title
-------------
Film Title 1
Film Title 2
```

- `title` - Film title