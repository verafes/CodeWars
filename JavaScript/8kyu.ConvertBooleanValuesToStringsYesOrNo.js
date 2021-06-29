// Solutions in JavaScript

// 8kyu - Convert boolean values to strings 'Yes' or 'No'

https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no

// Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false. 

function boolToWord( bool ){
  if (bool === true) {
	return "Yes";
  } else {
	return "No";
  }
}

// Solution 2:

function boolToWord( bool ){
  return (bool === true) ? "Yes" : "No";
}
