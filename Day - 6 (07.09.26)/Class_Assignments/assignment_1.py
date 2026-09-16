import threading
import time

# Lock
lock = threading.Lock()

def access_resource_lock(thread_name):
    with lock:
        print(f"{thread_name} entered")
        time.sleep(2)
        print(f"{thread_name} left")

threads = []

for i in range(3):
    thread = threading.Thread(target=access_resource_lock, args=(f"Thread-{i+1}",))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("\nSwitching to Semaphore\n")

# Semaphore
semaphore = threading.Semaphore(2)

def access_resource_semaphore(thread_name):
    with semaphore:
        print(f"{thread_name} entered ")
        time.sleep(2)
        print(f"{thread_name} left ")

threads = []

for i in range(4):
    thread = threading.Thread(target=access_resource_semaphore, args=(f"Thread-{i+1}",))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()