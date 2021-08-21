// Solutions in JavaScript

// 8kyu - Get Planet Name By ID

https://www.codewars.com/kata/515e188a311df01cba000003

/* The function is not returning the correct values. Can you figure out why?
Example (Input --> Output ):
3 --> "Earth"
*/ 

// Given:

function getPlanetName(id){
  var name;
  switch(id){
    case 1:
      name = 'Mercury'
    case 2:
      name = 'Venus'
    case 3:
      name = 'Earth'
    case 4:
      name = 'Mars'
    case 5:
      name = 'Jupiter'
    case 6:
      name = 'Saturn'
    case 7:
      name = 'Uranus'
    case 8:
      name = 'Neptune'
  }
  
  return name;
}

// Solution:

function getPlanetName(id){
  var name;
  switch(id){
    case 1: 
      return 'Mercury';
    case 2:
      return 'Venus';
    case 3:
      return'Earth';
    case 4:
      return 'Mars';
    case 5:
      return 'Jupiter';
    case 6:
      return 'Saturn';
    case 7:
      return 'Uranus';
    case 8:
      return 'Neptune';
  }
}

// Solution 2:

function getPlanetName(id){
  return {
    1: "Mercury",
    2: "Venus",
    3: "Earth",
    4: "Mars",
    5: "Jupiter",
    6: "Saturn",
    7: "Uranus",
    8: "Neptune",
  } [id];
}
