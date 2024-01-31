'''
Задание №7
� Напишите программу на Python, которая будет находить
сумму элементов массива из 1000000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами
от 1 до 100.
� При решении задачи нужно использовать многопоточность,
многопроцессорность и асинхронность.
� В каждом решении нужно вывести время выполнения
вычислений.

'''

''' многопоточный подход '''

from random import randint
import threading
import time


arr = [randint(1, 100) for _ in range(1_000_000)]

num_threads = 4

def calculate_sum(start, end, result):
    partial_sum = sum(arr[start:end])
    result.append(partial_sum)

start_time = time.time()


chunk_size = len(arr) // num_threads
chunks = [(i * chunk_size, (i + 1) * chunk_size) for i in range(num_threads - 1)]
chunks.append(((num_threads - 1) * chunk_size, len(arr)))


results = []


threads = []


for chunk in chunks:
    thread = threading.Thread(target=calculate_sum, args=(*chunk, results))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()


total_sum = sum(results)

end_time = time.time()

print("Сумма элементов массива:", total_sum)
print("Время выполнения:", end_time - start_time, "секунд")










