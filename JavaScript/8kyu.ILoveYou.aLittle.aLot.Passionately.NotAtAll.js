// Solutions in JavaScript

// 8kyu - I love you, a little , a lot, passionately ... not at all

https://www.codewars.com/kata/i-love-you-a-little-a-lot-passionately-dot-dot-dot-not-at-all

/* Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, 
saying each of the following phrases each time a petal was torn:

I love you
a little
a lot
passionately
madly
not at all
When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.

Your goal in this kata is to determine which phrase the girls would say for a flower of a given number of petals, where nb_petals > 0.
*/ 

function howMuchILoveYou(nbPetals) {
    nbPetals = nbPetals % 6;
      switch(nbPetals){
        case 1: return 'I love you';
        case 2: return 'a little';
        case 3: return 'a lot';
        case 4: return 'passionately';
        case 5: return 'madly';
        case 0: return 'not at all';
      }
}

// Solution 2:

function howMuchILoveYou(h) {
    h = h % 6;
    let arr = ["not at all", "I love you", "a little", "a lot", "passionately", "madly"];
    return arr[h];
}