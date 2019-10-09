# Become Immortal


## Instructions

In the nation of CodeWars, there lives an Elder who has lived for a long time. 
Some people call him the Grandpatriarch, but most people just refer to him as 
the Elder.

There is a secret to his longevity: he has a lot of young worshippers, who 
regularly perform a ritual to ensure that the Elder stays immortal:
- The worshippers lines up in a magic rectangle, of dimensions `m` and `n`.
- They channel their will to wish for the Elder. In this magic rectangle, any 
worshipper can donate time equal to the `xor` of the column and the row 
(zero-indexed) he's on, in seconds, to the Elder.
- However, not every ritual goes perfectly. The donation of time from the 
worshippers to the Elder will experience a transmission loss `l` (in seconds). 
Also, if a specific worshipper cannot channel more than `l` seconds, the Elder 
will not be able to receive this worshipper's donation.

The estimated age of the Elder is so old it's probably bigger than the total 
number of atoms in the universe. However, the lazy programmers (who made a big 
news by inventing the Y2K bug and other related things) apparently didn't think 
thoroughly enough about this, and so their simple date-time system can only 
record time from `0` to `t-1` seconds. If the elder received the total amount 
of time (in seconds) more than the system can store, it will be wrapped around 
so that the time would be between the range `0` to `t-1`.


### Task

Given `m`, `n`, `l` and `t`, please find the number of seconds the Elder has 
received, represented in the poor programmer's date-time system.



### Example

```
elder_age(8, 5, 1, 100) => 5


m=8, n=5, l=1, t=100

Let's draw out the whole magic rectangle:
0 1 2 3 4 5 6 7
1 0 3 2 5 4 7 6
2 3 0 1 6 7 4 5
3 2 1 0 7 6 5 4
4 5 6 7 0 1 2 3

Applying a transmission loss of 1:
0 0 1 2 3 4 5 6
0 0 2 1 4 3 6 5
1 2 0 0 5 6 3 4
2 1 0 0 6 5 4 3
3 4 5 6 0 0 1 2

Adding up all the time gives 105 seconds.

Because the system can only store time between 0 to 99 seconds, the first 100 
seconds of time will be lost, giving the answer of 5.
```


### Notes

- `t` will never be bigger than `2^32 - 1`.
- This is no ordinary magic (the Elder's life is at stake), so you need to care 
about performance. All test cases (900 tests) can be passed within 1 second, 
but naive solutions will time out easily. Good luck, and do not displease the 
Elder.