import time

while True:
    try:
        my_time = int(input("Enter the time in seconds: "))
        if my_time <= 0:
            print("Please enter a positive number for time.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid number for time.")
        
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is out!")