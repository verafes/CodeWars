# Solutions in Python

# 8kyu - Fix your code before the garden dies!

https://www.codewars.com/kata/57158fb92ad763bb180004e7 

# You have an award-winning garden and everyday the plants need exactly 40mm of water. 
# You created a great piece of JavaScript to calculate the amount of water your plants will need 
# when you have taken into consideration the amount of rain water that is forecast for the day. 
# Your jealous neighbour hacked your computer and filled your code with bugs.
# Your task is to debug the code before your plants die!

# Given

function rainAmount(mm){
    if (rainAmount = 40) {
         return "You need to give your plant " + {rainAmount - 40} + " mm of water"
    };
    if else {
         return "Your plant has had more than enough water for today!"
    };
}

# Solution

def rain_amount(mm):
    if mm < 40:
         return f"You need to give your plant {40 - mm}mm of water"
    else:
         return "Your plant has had more than enough water for today!"


