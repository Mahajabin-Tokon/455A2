import time

def timelimit(seconds):
    if not (1 <= seconds <=100):
        print("Wrong")
        # self.respond("The argument of the function should be an integer in the range 1 <= seconds <= 100.")
    return seconds
        
t = timelimit(10)

while t > 0:
    print(t)
    t -= 1
    time.sleep(1)
print("BLAST OFF!")

