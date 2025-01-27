import time

def format_time(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}.{int((seconds % 1) * 1000):03}"

start_time = 0
elapsed_time = 0
running = False

print("Welcome to the Python Stopwatch Program!")
print('Type "start" to begin, "stop" to pause, "reset" to reset, and "exit" to quit.')

while True:
    command = input("Enter a command: ").strip().lower()
    
    if command == "start":
        if not running:
            start_time = time.perf_counter() - elapsed_time
            running = True
            print("Stopwatch started!")
        else:
            print("Stopwatch is already running.")
    
    elif command == "stop":
        if running:
            elapsed_time = time.perf_counter() - start_time
            running = False
            print(f"Stopwatch paused at: {format_time(elapsed_time)}")
        else:
            print("Stopwatch is not running.")
    
    elif command == "reset":
        if running:
            elapsed_time = 0
            start_time = time.perf_counter()
        else:
            elapsed_time = 0
        print("Stopwatch reset.")
    
    elif command == "exit":
        print("Goodbye!")
        break
    
    else:
        print("Invalid command. Please type 'start', 'stop', 'reset', or 'exit'.")
    
    if running:
        current_time = time.perf_counter() - start_time
        print(format_time(current_time), end="\r")
        time.sleep(0.1)
