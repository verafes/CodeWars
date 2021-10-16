// Solutions in JavaScript

// 7kyu - Factorial

https://www.codewars.com/kata/factorial-1

// Your task is to write function factorial.

function factorial(n){
  let i = n, f = 1;
  while (i > 0) { 
    f = f * i;
    i--;
  }
  return f;
}