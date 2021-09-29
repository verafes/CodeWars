// Solutions in JavaScript

// 7kyu - Going to the cinema

https://www.codewars.com/kata/562f91ff6a8b77dfe900006e

/* My friend John likes to go to the cinema. He can choose between system A and system B.

System A : he buys a ticket (15 dollars) every time
System B : he buys a card (500 dollars) and a first ticket for 0.90 times the ticket price, 
then for each additional ticket he pays 0.90 times the price paid for the previous ticket.
Example:
If John goes to the cinema 3 times:

System A : 15 * 3 = 45
System B : 500 + 15 * 0.90 + (15 * 0.90) * 0.90 + (15 * 0.90 * 0.90) * 0.90 ( = 536.5849999999999, no rounding for each ticket)
John wants to know how many times he must go to the cinema so that the final result of System B, when rounded up to the next dollar, 
will be cheaper than System A.

The function movie has 3 parameters: card (price of the card), ticket (normal price of a ticket), 
perc (fraction of what he paid for the previous ticket) and returns the first n such that
ceil(price of System B) < price of System A.
*/ 

function movie(card, ticket, perc) {
  let sumA = 0;
  let sumB = card;
  let count = 0;
  let ticketB = ticket;
  while (sumA <= Math.ceil(sumB)) {
    sumA = sumA + ticket;
    ticketB = ticketB * perc;
    sumB = sumB + ticketB;
    count++;
  }
  return count
};