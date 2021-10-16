// Solutions in JavaScript

// 7kyu - Largest prime number containing n digit

https://www.codewars.com/kata/5676f07029da352ba2000065

/* Just as the title suggestes :D . For example ->

largest(1); //Should return 7
largest(2); //Should return 97
....
Do not mind the pattern as it is just an incident ! 
And make sure to return false if the input is not an integer :D 
This might seem simple at first, it is, but keep an eye on the performance. Go for it !
*/ 

function isPrime(num) {
  for (let i = 2; i * i <= num; i++) {
    if (num % i === 0) return false; 
  }
  return num > 1;
}

const largest = (n) => {
  if (typeof n != 'number' || n < 1) return false;
  let num = 10**n-1;
  while (isPrime(num) != true) {
    num -= 1;
  } 
  return num;
}