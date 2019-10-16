# Challenge: Two Actors Who Cast Together the Most


## Instructions

Given the the schema presented below find two actors who cast together
the most and list titles of only those movies they were casting
together. Order the result set alphabetically by the movie title.


### Table Schemas

```
film_actor Table Schema

 Column     | Type                        | Modifiers
------------+-----------------------------+----------
actor_id    | smallint                    | not null
film_id     | smallint                    | not null
```

```
actor Table Schema

 Column     | Type                        | Modifiers
------------+-----------------------------+----------
actor_id    | integer                     | not null
first_name  | character varying(45)       | not null
last_name   | character varying(45)       | not null
```

```
film Table Schema

 Column     | Type                        | Modifiers
------------+-----------------------------+----------
film_id     | integer                     | not null
title       | character varying(255)      | not null
```

```
output Table Schema
- first_actor: Full name (First name + Last name separated by a space)
- second_actor: Full name (First name + Last name separated by a space)
- title: Movie title

first_actor | second_actor | title
------------+--------------+--------------------
John Doe    | Jane Doe     | The Best Movie Ever
```


### Note
`actor_id` of the first_actor should be lower than `actor_id` of the
second_actor.