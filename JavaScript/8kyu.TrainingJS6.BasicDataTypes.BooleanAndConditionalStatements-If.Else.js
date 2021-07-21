// Solutions in JavaScript

// 8kyu - Training JS #6: Basic data types--Boolean and conditional statements if..else

https://www.codewars.com/kata/training-js-number-6-basic-data-types-boolean-and-conditional-statements-if-dot-else

/* Task
Coding in function trueOrFalse, function accept 1 parameters:val, try to use the conditional statement if...else, if val value is false (val==false or it can convert to false), should return a string "false", if not, return a string "true".

When you have finished the work, click "Run Tests" to see if your code is working properly.

In the end, click "Submit" to submit your code pass this kata.
*/ 

// Solution 1:

function trueOrFalse(val){
  return Boolean(val).toString();
}


// Solution 2:

function trueOrFalse(val){
  if (val) return "true";             
  else return "false";
}
