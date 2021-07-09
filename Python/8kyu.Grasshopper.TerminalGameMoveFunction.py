# Solutions in Python

# 8kyu - Grasshopper - Terminal game move function

https://www.codewars.com/kata/563a631f7cbbc236cf0000c2/train/python

# In this game, the hero moves from left to right. 
# The player rolls the dice and moves the number of spaces indicated by the dice two times.
# Create a function for the terminal game that takes the current position of the hero 
# and the roll (1-6) and return the new position.

# Example:
# move(3, 6) should equal 15

def move(position, roll):
  if roll < 1 or roll > 6:
    return "Error"
  else:
    new_position = position + (roll * 2)
    return(new_position)
