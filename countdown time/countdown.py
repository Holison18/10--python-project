# This is a simple timer create in python
import time

# create a countdown function to countdown the timer
def countDown(t:int):

    # loop through the time and print it out while time is not zero
    while t:
        mins,secs = divmod(t,60)
        timer = "{:02d}:{:02d}".format(mins,secs)
        print(timer,end="\r")
        t-=1
    print("Fire in the hole!!!")

