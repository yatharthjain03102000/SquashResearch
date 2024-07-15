import time
import random
from playsound import playsound

# First part: Generate a random number every 4.6154 seconds for 60 seconds
start_time = time.time()
end_time = start_time + 10  # 60 seconds later

while time.time() < end_time:
    number = random.randint(1, 4)
    playsound(f"sounds/{number}.mp3")
    print(f"Number: {number}")
    time.sleep(4.6154)

playsound("sounds/Beep.mp3")
print("Transition 1 starting")

# Second part: Generate a random number every 4.2857 seconds for the next 60 seconds
start_time = time.time()
end_time = start_time + 10  # 60 seconds later

while time.time() < end_time:
    number = random.randint(1, 4)
    playsound(f"sounds/{number}.mp3")
    print(f"Number: {number}")
    time.sleep(4.2857)

playsound("sounds/Beep.mp3")
print("Transition 2 starting")

start_time = time.time()
end_time = start_time + 10  # 60 seconds later

while time.time() < end_time:
    number = random.randint(1, 4)
    playsound(f"sounds/{number}.mp3")
    print(f"Number: {number}")
    time.sleep(4.0000)

playsound("sounds/Beep.mp3")
print("Transition 3 starting")

start_time = time.time()
end_time = start_time + 10  # 60 seconds later

while time.time() < end_time:
    number = random.randint(1, 4)
    playsound(f"sounds/{number}.mp3")
    print(f"Number: {number}")
    time.sleep(3.7500)

playsound("sounds/Beep.mp3")
print("Transition 4 starting")

start_time = time.time()
end_time = start_time + 10  # 60 seconds later

while time.time() < end_time:
    number = random.randint(1, 4)
    playsound(f"sounds/{number}.mp3")
    print(f"Number: {number}")
    time.sleep(3.5294)

playsound("sounds/Beep.mp3")
print("Transition 5 starting")

start_time = time.time()
end_time = start_time + 10  # 60 seconds later

while time.time() < end_time:
    number = random.randint(1, 4)
    playsound(f"sounds/{number}.mp3")
    print(f"Number: {number}")
    time.sleep(3.3333)

playsound("sounds/Beep.mp3")
print("Transition 6 starting")

start_time = time.time()
end_time = start_time + 10  # 60 seconds later

while time.time() < end_time:
    number = random.randint(1, 4)
    playsound(f"sounds/{number}.mp3")
    print(f"Number: {number}")
    time.sleep(3.1589)

playsound("sounds/Beep.mp3")
print("Transition 7 starting")

start_time = time.time()
end_time = start_time + 10  # 60 seconds later

while time.time() < end_time:
    number = random.randint(1, 4)
    playsound(f"sounds/{number}.mp3")
    print(f"Number: {number}")
    time.sleep(3.0000)

playsound("sounds/Beep.mp3")
print("Transition 8 starting")

start_time = time.time()
end_time = start_time + 10  # 60 seconds later

while time.time() < end_time:
    number = random.randint(1, 4)
    playsound(f"sounds/{number}.mp3")
    print(f"Number: {number}")
    time.sleep(2.8571)

playsound("sounds/Beep.mp3")
print("Transition 9 starting")

start_time = time.time()
end_time = start_time + 10  # 60 seconds later

while time.time() < end_time:
    number = random.randint(1, 4)
    playsound(f"sounds/{number}.mp3")
    print(f"Number: {number}")
    time.sleep(2.7273)

playsound("sounds/Beep.mp3")
print("Transition 10 starting")

start_time = time.time()
end_time = start_time + 10  # 60 seconds later

while time.time() < end_time:
    number = random.randint(1, 4)
    playsound(f"sounds/{number}.mp3")
    print(f"Number: {number}")
    time.sleep(2.6087)
