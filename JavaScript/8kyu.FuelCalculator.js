// Solutions in JavaScript

// 8kyu - Fuel Calculator

https://www.codewars.com/kata/57b58827d2a31c57720012e8

/* n this kata you will have to write a function that takes litres and pricePerLitre as arguments. 
Purchases of 2 or more litres get a discount of 5 cents per litre, 
purchases of 4 or more litres get a discount of 10 cents per litre, 
and so on every two litres, up to a maximum discount of 25 cents per litre. 
But total discount per litre cannot be more than 25 cents. 
Return the toal cost rounded to 2 decimal places. 
Also you can guess that there will not be negative or non-numeric inputs.
*/ 

function fuelPrice(litres, pricePerLitre) {
  let sale;
  if (litres < 2) sale = 0;
  else if (litres < 4) sale = 0.05;
  else if (litres < 6) sale = 0.10;
  else if (litres < 8) sale = 0.15;
  else if (litres < 10) sale = 0.20;
  else sale = 0.25;
  return +(litres * (pricePerLitre - sale)).toFixed(2); 
}
