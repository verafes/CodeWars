# Solutions in Python

# 6kyu - Cat and Mouse - Harder Version

https://www.codewars.com/kata/57ee2a1b7b45efcf700001bf 

# You will be given a string (x) featuring a cat 'C', a dog 'D' and a mouse 'm'. The rest of the string will be made up of '.'.
# You need to find out if the cat can catch the mouse from it's current position. The cat can jump (j) characters.
# Also, the cat cannot jump over the dog.
# So: if j = 5:
# ..C.....m. returns 'Caught!' <-- not more than j characters between
# .....C............m...... returns 'Escaped!' <-- as there are more than j characters between the two, the cat can't jump far enough
# if j = 10:
# ...m.........C...D returns 'Caught!' <--Cat can jump far enough and jump is not over dog
# ...m....D....C....... returns 'Protected!' <-- Cat can jump far enough, but dog is in the way, protecting the mouse
# Finally, if all three animals are not present, return 'boring without all three'

def cat_mouse(x,j):
    cat = x.index("C") if x.count("C") == 1 else 0
    dog = x.index("D") if x.count("D") == 1 else 0
    mouse = x.index("m") if x.count("m") == 1 else 0
    if cat == 0 or dog == 0 or mouse == 0:
        return "boring without all three"
    elif (cat < dog < mouse or mouse < dog < cat):
        if abs(cat-mouse)<= j:
            return "Protected!"
        else:
            return "Escaped!"
    elif abs(cat-mouse)<= j:
        return "Caught!"
    else:
        return "Escaped!"
