import multiprocessing
import time

def task1():
    for _ in range(5):
        print("Выполняется задача 1")
        time.sleep(1)

def task2():
    for _ in range(5):
        print("Выполняется задача 2")
        time.sleep(1)

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=task1)
    process2 = multiprocessing.Process(target=task2)

    process1.start()
    process2.start()

    process1.join()
    process2.join()

    print("Обе задачи завершены.")