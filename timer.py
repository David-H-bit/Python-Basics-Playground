import time, os, sys

my_time = int(input("Enter how long the timer should last in seconds: "))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    sys.stdout.write(f"\r{hours:02}:{minutes:02}:{seconds:02}")
    sys.stdout.flush()
    time.sleep(1)

print()
os.system("say 'Time is up!'") # for windows use winsound.Beep(x, y) (x = frequency in Hertz, y = duration in ms) and import winsounds
print("Time is up!")