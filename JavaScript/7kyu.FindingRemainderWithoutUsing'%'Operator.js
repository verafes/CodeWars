// Solutions in JavaScript

// 7kyu - Finding Remainder Without Using '%' Operator

https://www.codewars.com/kata/564f458b4d75e24fc9000041

/* Task
Write a method remainder which takes two integer arguments, dividend and divisor, 
and returns the remainder when dividend is divided by divisor. 
Do NOT use the modulus operator (%) to calculate the remainder!

Assumption
Dividend will always be greater than or equal to divisor.

Notes
Make sure that the implemented remainder function works exactly the same as the Modulus operator (%).
*/ 

function remainder (D, d){
  while (D >= d ) D -= d;
  return D;
}
