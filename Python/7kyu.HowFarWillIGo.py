# Solutions in Python

# 7kyu - How far will I go?

https://www.codewars.com/kata/56d46b8fda159582e100001b

# You have recently discovered that horses travel in a unique pattern - they're either running (at top speed) or resting (standing still).
# Here's an example of how one particular horse might travel:
# The horse Blaze can run at 14 metres/second for 60 seconds, but must then rest for 45 seconds.
# After 500 seconds Blaze will have traveled 4200 metres.
# Your job is to write a function that returns how long a horse will have traveled after a given time.

####Input:
# totalTime - How long the horse will be traveling (in seconds)
# runTime - How long the horse can run for before having to rest (in seconds)
# restTime - How long the horse have to rest for after running (in seconds)
# speed - The max speed of the horse (in metres/second)

def travel(total_time, run_time, rest_time, speed):
    one_round = run_time +  rest_time
    number_round = total_time//one_round
    dist_one_round = run_time * speed
    total_dist = number_round * dist_one_round
    reminder = total_time % one_round
    if reminder >= run_time:
        total_dist += dist_one_round
    else:
        total_dist += reminder * speed
    return total_dist
