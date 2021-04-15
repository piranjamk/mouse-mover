import keyboard
import pyautogui as pa
import time
import random


def get_time():
    return round(time.time())


print("Press q or esc to exit.")
time.sleep(1)
print("Start in:")
for i in reversed(range(10)):
    print(i)
    time.sleep(1)
    if keyboard.is_pressed('esc') or keyboard.is_pressed('q'):
        print("The end")
        print("GREETINGS FROM \~ZIOMBELEK~/")
        time.sleep(5)
        exit()
start_time = time.time()
random.seed()
screen = pa.size()
counter = 1
screen_height = screen[0]
screen_width = screen[1]
seconds = random.randint(1, 15)
previous_time = get_time()
while 1:
    if keyboard.is_pressed('esc') or keyboard.is_pressed('q'):
        break
    if get_time() - previous_time > seconds:
        previous_time = time.time()
        seconds = random.randint(1, 15)
        x = random.randint(7, screen_width - 195)
        y = random.randint(7, int(screen_height/2))
        movement_time = random.random() + random.random() + random.random()
        pa.moveTo(x,y, movement_time)
        czas = time.time() - start_time
        print("Timer:: ", int(czas/60/60), "h ", int(czas/60), "m ", int(czas) % 60, "s")
        if 1 <= counter <= 5:
            pa.scroll(113)
        if 6 <= counter <= 10:
            pa.scroll(-113)
        if counter == 10:
            counter = 0
        counter += 1
print("The end")
pa.moveTo(1, 1, 0.1)
print("GREETINGS FROM \~ZIOMBELEK~/")
time.sleep(5)

