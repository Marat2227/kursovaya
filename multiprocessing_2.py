import asyncio

async def task1():
    for _ in range(5):
        print("Выполняется задача 1")
        await asyncio.sleep(1)

async def task2():
    for _ in range(5):
        print("Выполняется задача 2")
        await asyncio.sleep(1)

async def main():
    задачи = [task1(), task2()]
    await asyncio.gather(*задачи)

if __name__ == "__main__":
    asyncio.run(main())