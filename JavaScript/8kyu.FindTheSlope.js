// Solutions in JavaScript

// 8kyu - Find the Slope

https://www.codewars.com/kata/find-the-slope

/* Given an array of 4 integers
[a,b,c,d] representing two points (a, b) and (c, d), return a string representation of the slope of the line joining these two points.
For an undefined slope (division by 0), return undefined . Note that the "undefined" is case-sensitive.
   a:x1
   b:y1
   c:x2
   d:y2
Assume that [a,b,c,d] and the answer are all integers (no floating numbers!).
*/ 

function slope(points) { let a = points[0]
  let b = points[1] 
  let c = points[2]
  let d = points[3]

  if (a == c) { 
    return 'undefined';
  } else {
    return (+((b - d) / (a - c))) + "";
  }
}
// Solution 2

function slope(points) {
  let sum = (points[1] - points[3]) / (points[0] - points[2]);
  let sumString = sum.toString();
  return points[0] === points[2] ? 'undefined' : sumString;
}
