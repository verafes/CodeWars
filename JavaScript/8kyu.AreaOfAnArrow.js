// Solutions in JavaScript

// 8kyu - Area of an arrow

https://www.codewars.com/kata/589478160c0f8a40870000bc

/* An arrow is formed in a rectangle with sides a and b 
by joining the bottom corners to the midpoint of the top edge and the centre of the rectangle.
----------
|        |
|        |
|        |
|   /\   | b
|  /  \  |
| /    \ |
|/arrow \|
----------
    a	
*/ 

function arrowArea(a,b) {
  return a * b / 4;
}

