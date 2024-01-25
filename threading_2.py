import concurrent.futures
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
    with concurrent.futures.ThreadPoolExecutor() as executor:
        tasks = [executor.submit(task1), executor.submit(task2)]

        concurrent.futures.wait(tasks, return_when=concurrent.futures.ALL_COMPLETED)

    print("Обе задачи завершены.")