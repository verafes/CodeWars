// Solutions in JavaScript

// 8kyu - Training JS #7: if..else and ternary operator

https://www.codewars.com/kata/training-js-number-7-if-dot-else-and-ternary-operator

/* Task:
Complete function saleHotdogs/SaleHotDogs/sale_hotdogs, function accept 1 parameters:
n, n is the number of customers to buy hotdogs, different numbers have different prices 
(refer to the following table), return a number that the customer need to pay how much money.

+---------------+-------------+
|  numbers n    | price(cents)|
+---------------+-------------+
|n<5            |    100      |
+---------------+-------------+
|n>=5 and n<10  |     95      |
+---------------+-------------+
|n>=10          |     90      |
+---------------+-------------+

You can use if..else or ternary operator to complete it.

*/ 

function saleHotdogs(n){
  return n * ((n < 5) ? 100 : (n < 10) ? 95 : 90);
}
