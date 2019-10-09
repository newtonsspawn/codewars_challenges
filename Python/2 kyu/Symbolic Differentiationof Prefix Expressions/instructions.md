# Symbolic Differentiation of Prefix Expressions


## Instructions

In this kata your task is to differentiate a mathematical expression given as a 
string in prefix notation. The result should be the derivative of the 
expression returned in prefix notation.

To simplify things we will use a simple list format made up of parenthesis and 
spaces.
- The expression format is (func arg1) or (op arg1 arg2) where op means 
operator, func means function and arg1, arg2 are arguments to the operator or 
function.
  - For example (+ x 1) or (cos x)
- The expressions will always have balanced parenthesis and with spaces between 
list items.
- Expression operators, functions and arguments will all be lowercase.
- Expressions are single variable expressions using `x` as the variable.
- Expressions can have nested arguments at any depth for example 
`(+ (* 1 x) (* 2 (+ x 1)))`.

Examples of prefix notation in this format:
```
(+ x 2)        // prefix notation version of x+2

(* (+ x 3) 5)  // same as 5 * (x + 3)

(cos (+ x 1))  // same as cos(x+1)

(^ x 2)        // same as x^2 meaning x raised to power of 2
```

The operators and functions you are required to implement are 
`+ - * / ^ cos sin tan exp ln` where `^` means raised to power of. `exp` is the 
exponential function (same as `e^x`) and `ln` is the natural logarithm (base e).


### Examples

Example of input values and their derivatives:
```
(* 1 x) => 1

(^ x 3) => (* 3 (^ x 2))

(cos x) => (* -1 (sin x))
```


### Notes

In addition to returning the derivative your solution must also do some 
simplifications of the result but only what is specified below.
- The returned expression should not have unecessary 0 or 1 factors. For 
example it should not return `(* 1 (+ x 1))` but simply the term `(+ x 1)` 
similarly it should not return `(* 0 (+ x 1))` instead it should return just 
`0`.
- Results with two constant values such as for example `(+ 2 2)` should be 
evaluated and returned as a single value `4`.
- Any argument raised to the zero power should return `1` and if raised to 1 
should return the same value or variable. For example `(^ x 0)` should return 
`1` and `(^ x 1)` should return `x`.
- No simplifications are expected for functions like `cos`, `sin`, `exp`, 
`ln`... (but their arguments might require a simplification).

Think recursively and build your answer according to the 
[rules of derivation](http://www.rapidtables.com/math/calculus/derivative.htm) 
and sample test cases.

If you need to diff_ref_02 any test expressions you can use 
[Wolfram Alpha](http://www.wolframalpha.com/) however remember we use prefix 
format in this kata.

Best of luck !