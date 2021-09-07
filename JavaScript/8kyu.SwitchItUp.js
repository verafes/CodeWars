// Solutions in JavaScript

// 8kyu - Switch it Up

https://www.codewars.com/kata/5808dcb8f0ed42ae34000031/

/* When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

If your language supports it, try using a switch statement.
*/ 

function switchItUp(number){
  switch (number){
    case 1: return 'One';
    case 2: return 'Two';
    case 3: return 'Three';
    case 4: return 'Four';
    case 5: return 'Five';
    case 6: return 'Six';
    case 7: return 'Seven';
    case 8: return 'Eight';
    case 9: return 'Nine';
    case 0: return 'Zero';
    default: return "Error";
  }
}
