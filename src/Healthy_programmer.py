"""
IMPORTANT ===> before use this code change the time according to your convenience.
<===================================================================================>

line number => 55 -> time for drink water.
line number => 56 -> time for eye exercise.
line number => 56 -> time for physical exercise.
"""


import playAudio
import time
from datetime import datetime

def L_time(s_time, e_time):
    diff = e_time - s_time
    time_interval = (0.250 * diff) / 3
    l_time = int(diff / time_interval)
    return l_time

def get_time():
    curr_time = datetime.now()
    return curr_time

def drink_water():
    print("It's time to drink water!\nEnter 'Drank' for conformation.")

    playAudio.playAudio("Water.mp3", "drank")

    w_time = get_time()
    with open("water.txt", "a") as w:
        w.write(f"You drank 250ml at {w_time}.\n")
    
def eye_exercise():
    print("It's time to do eye exercise!\nEnter 'eye done' for stop reminder.")

    playAudio.playAudio("eye_exercise.mp3", "eye done")

    eye_time = get_time()
    with open("eye_exercise.txt", "a") as eye:
        eye.write(f"You did eye exercise at {eye_time}.\n")

def physical():
    print("It's time to do physical exercise!\nEnter 'physic done' for stop reminder.")

    playAudio.playAudio("workout.mp3", "physic done")

    physic_time = get_time()
    with open("physical.txt", "a") as physic:
        physic.write(f"You did physica exercise at {physic_time}.\n")

print("Enter your office time (24 hour formate) ")
start_time = int(input("Enter the start time : "))
end_time = int(input("Enter the end time : "))

water_time = 5
eye_time = 10
exercise_time = 15

start_water = time.time()
start_eye = time.time()
start_exercise = time.time()

loop_times = L_time(start_time, end_time)
flag = 0

while True:
    
    if time.time() - start_water > water_time:
        drink_water()
        start_water = time.time()
        flag += 1

    if time.time() - start_eye > eye_time:
        eye_exercise()
        start_eye = time.time()

    if time.time() - start_exercise > exercise_time:
        physical()
        start_exercise = time.time()

    if flag >= loop_times:
        break
