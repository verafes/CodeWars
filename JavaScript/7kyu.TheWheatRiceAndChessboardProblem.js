// Solutions in JavaScript

// 7kyu - The wheat/rice and chessboard problem

https://www.codewars.com/kata/the-wheat-slash-rice-and-chessboard-problem

/* I assume most of you are familiar with the ancient legend of the rice (but I see wikipedia suggests wheat, for some reason) problem, 
but a quick recap for you: a young man asks as a compensation only 1 grain of rice for the first square, 2 grains for the second, 
4 for the third, 8 for the fourth and so on, always doubling the previous.

Your task is pretty straightforward (but not necessarily easy): given an amount of grains, 
you need to return up to which square of the chessboard one should count in order to get at least as many.

As usual, a few examples might be way better than thousands of words from me:

squaresNeeded(0) === 0
squaresNeeded(1) === 1
squaresNeeded(2) === 2
squaresNeeded(3) === 2
squaresNeeded(4) === 3
Input is always going to be valid/reasonable: ie: a non negative number; 
extra cookie for not using a loop to compute square-by-square (at least not directly) and instead trying a smarter approach 
[hint: some peculiar operator]; a trick converting the number might also work: impress me!
*/ 

function squaresNeeded(grains){
  let count = 0; 
  let grainInCell =  1;
  while (grains > 0) {
    grains -= grainInCell;
    grainInCell *= 2;
    count++;
  }
  return count
}

// Solution #2:

function squaresNeeded(grains){
  let squares = 0;
  while (2**squares <= grains) {
    squares += 1;
  }
  return squares;
}
 