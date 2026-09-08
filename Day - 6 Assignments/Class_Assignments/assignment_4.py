import threading
from multiprocessing import Process

def threading_task(name):
    print(f"{name} started ")
    print(f"{name} finished ")

def multiprocessing_task(name):
    print(f"{name} started")
    print(f"{name} finished")

def main():
    # Threading
    thread1 = threading.Thread(target=threading_task, args=("Task A",))
    thread2 = threading.Thread(target=threading_task, args=("Task B",))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("\nSwitching to Multiprocessing\n")

    # Multiprocessing
    process1 = Process(target=multiprocessing_task, args=("Task A",))
    process2 = Process(target=multiprocessing_task, args=("Task B",))

    process1.start()
    process2.start()

    process1.join()
    process2.join()

if __name__ == "__main__":
    main()