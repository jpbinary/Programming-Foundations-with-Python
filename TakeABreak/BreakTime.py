import time
import webbrowser

NUMBER_OF_BREAKS = 3
current_break = 1
print("This program began on: " + time.ctime())
while current_break <= NUMBER_OF_BREAKS:
    time.sleep(60*90)
    print("Time to take a break!")
    webbrowser.open("https://www.youtube.com/watch?v=V1bFr2SWP1I")
    current_break += 1
