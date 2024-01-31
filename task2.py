'''
многопроцессорный подход
'''

from random import randint
import multiprocessing
import time


arr = [randint(1, 100) for _ in range(1_000_000)]

num_processes = 4

def calculate_sum(start, end, result):
    partial_sum = sum(arr[start:end])
    result.append(partial_sum)


if __name__ == '__main__':

    start_time = time.time()

    manager = multiprocessing.Manager()
    results = manager.list()


    chunk_size = len(arr) // num_processes
    chunks = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_processes - 1)]
    chunks.append(((num_processes - 1) * chunk_size, len(arr)))


    processes = []


    for chunk in chunks:
        process = multiprocessing.Process(target=calculate_sum, args=(*chunk, results))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()


    total_sum = sum(results)

    end_time = time.time()

    print("Сумма элементов массива:", total_sum)
    print("Время выполнения:", end_time - start_time, "секунд")

'''
Сумма элементов массива: 50511065
Время выполнения: 0.9631435871124268 секунд
'''