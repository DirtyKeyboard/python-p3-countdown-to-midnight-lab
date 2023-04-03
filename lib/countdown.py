# your code goes here!
import time

def countdown(time):
    while time > 0:
        print(f'{time} SECOND(S)!')
        time -= 1
    print('HAPPY NEW YEAR!')

def countdown_with_sleep(t):
    while t > 0:
        print(f'{t} SECOND(S)!')
        time.sleep(1)
        t -= 1
    print('HAPPY NEW YEAR!')