'''
асинхронный подход
'''

from random import randint
import asyncio
import time


arr = [randint(1, 100) for _ in range(1_000_000)]

num_async = 4

async def calculate_sum(start, end, result):
    partial_sum = sum(arr[start:end])
    result.append(partial_sum)


async def main():

    start_time = time.time()

    
    results = []


    chunk_size = len(arr) // num_async
    chunks = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_async - 1)]
    chunks.append(((num_async - 1) * chunk_size, len(arr)))


    tasks = []


    for chunk in chunks:
        task = asyncio.create_task(calculate_sum(*chunk, results))
        tasks.append(task)

    await asyncio.gather(*tasks)


    total_sum = sum(results)

    end_time = time.time()

    print("Сумма элементов массива:", total_sum)
    print("Время выполнения:", end_time - start_time, "секунд")

if __name__ == '__main__':
    asyncio.run(main())


'''
Сумма элементов массива: 50596285
Время выполнения: 0.0050051212310791016 секунд
'''