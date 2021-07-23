// Solutions in JavaScript

// 7kyu - Find the sum of the roots of a quadratic equation

https://www.codewars.com/kata/57d448c6ba30875437000138

/* Implement function which will return sum of roots of a quadratic equation rounded to 2 decimal places, 
if there are any possible roots, else return None/null/nil/nothing. 
If you use discriminant,when discriminant = 0, x1 = x2 = root => return sum of both roots. 
There will always be valid arguments.
*/ 

// Solution 1:

function roots(a,b,c){
  let root1, root2;
  let discriminant = b * b - 4 * a * c;
  if (discriminant > 0) {
    root1 = (-b + Math.sqrt(discriminant)) / (2 * a);
    root2 = (-b - Math.sqrt(discriminant)) / (2 * a);
    return +(root1 + root2).toFixed(2);
  }
  else if (discriminant == 0) {
    root1 = root2 = -b / (2 * a);
    return (root1 + root2);
  }
  else return null;
}

// Solution 2:

function roots(a,b,c){
  let d = b*b - 4 * a * c;
  if (d < 0) return null;
  return +(-b/a).toFixed(2);
}
