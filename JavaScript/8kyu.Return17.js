// Solutions in JavaScript

// 8kyu - Return 17

https://www.codewars.com/kata/57f022a6cba9da84a3000095

/* You are given a function named return17.
You should fix the if expression so the function will return 17, 
by making exactly two modifications: add one character and remove one character.
Good luck! */ 

// Given:

var return17 = function() {
  var a = 1; if (a = 5000); return 13; return 17;
}

// Solution:

var return17 = function() {
  var a = 1; if (a >= 5000) return 13; return 17;
}