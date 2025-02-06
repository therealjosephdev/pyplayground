# multithreading = Used to perform multiple tasks concurrently (multitasking)
#                  Good for I/O bound tasks like reading files or fetching data from APIs
#                  threading.Thread(target=my_function)

import threading
import time

def walk_dog(first, last):
    time.sleep(8)
    print(f"You finish walking {first} {last}.")
    
def take_out_trash():
    time.sleep(2)
    print("You take out trash.")
    
def get_mail():
    time.sleep(4)
    print("You get the mail.")
    
chore_one = threading.Thread(target=walk_dog, args=("Scooby", "Doo"))
chore_one.start()

chore_two = threading.Thread(target=take_out_trash)
chore_two.start()

chore_three = threading.Thread(target=get_mail)
chore_three.start()

chore_one.join()
chore_two.join()
chore_three.join()

print("ALL CHORES ARE COMPLETE!")