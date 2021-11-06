// Solutions in JavaScript

// 7kyu - Next Prime

https://www.codewars.com/kata/58e230e5e24dde0996000070

/* Get the next prime number!
You will get a numbern (>= 0) and your task is to find the next prime number.
Make sure to optimize your code: there will numbers tested up to about 10^12.

Examples
5   =>  7
12  =>  13
*/ 

function isPrime(n) {
  if (n <= 1) return false;
  for (let i = 2; i < Math.round(n**0.5 + 1); i++) {
    if (n % i === 0) return false; 
  }
  return true;
}

function nextPrime(n){
  n += 1;
  while (!isPrime(n)) n++;  
  return n
}