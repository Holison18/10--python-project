import time

# define a function countdown() with one parameter t
def countdown(t):

    while t:
        mins,secs = divmod(t,60)
        timer = "{:02d}:{:02d}".format(mins,secs)
        print(timer,end="\r")
        time.sleep(1)
        t-=1
    print("Fire in the hole!")

# ask user to enter time in seconds
time_in_secs = int(input("Enter time in seconds: "))
countdown(time_in_secs)