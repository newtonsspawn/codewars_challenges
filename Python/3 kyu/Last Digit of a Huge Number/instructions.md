# Last Digit of a Huge Number


## Instructions

For a given list `[x1, x2, x3, ..., xn]` compute the last (decimal) digit of 
`x1 ^ (x2 ^ (x3 ^ (... ^ xn)))`.


### Example

```
last_digit([3, 4, 2]) == 1
```

because `3 ^ (4 ^ 2) = 3 ^ 16 = 43046721`.


### Notes

**Beware**: powers grow incredibly fast. For example,` 9 ^ (9 ^ 9)` has more 
than 369 millions of digits. `last_digit` has to deal with such numbers 
efficiently.

**Corner cases**: we assume that `0 ^ 0 = 1` and that `last_digit` of an empty 
list equals to `1`.
