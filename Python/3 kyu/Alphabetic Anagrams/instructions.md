# Instructions

Consider a "word" as any sequence of capital letters A-Z (not limited to just 
"dictionary words"). For any word with at least two different letters, there 
are other words composed of the same letters but in a different order (for 
instance, STATIONARILY/ANTIROYALIST, which happen to both be dictionary words; 
for our purposes "AAIILNORSTTY" is also a "word" composed of the same letters 
as these two).

We can then assign a number to every word, based on where it falls in an 
alphabetically sorted list of all words made up of the same group of letters. 
One way to do this would be to generate the entire list of words and find the 
desired one, but this would be slow if the word is long.

Given a word, return its number. Your function should be able to accept any 
word 25 letters or less in length (possibly with some letters repeated), and 
take no more than 500 milliseconds to run. To compare, when the solution code 
runs the 27 test cases in JS, it takes 101ms.


## Notes

Python, Java, and Haskell have arbitrary integer precision, so you must be 
precise in those languages (unless someone corrects me).


## Examples

Sample words, with their rank:
```
ABAB = 2
AAAB = 1
BAAA = 4
QUESTION = 24572
BOOKKEEPER = 10743
```