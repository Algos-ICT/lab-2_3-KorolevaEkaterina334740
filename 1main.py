import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


def explore(x):
    visited[x] = True
    for apex in graph[x]:
        if not visited[apex]:
            explore(apex)


if __name__ == '__main__':
    graph = dict()
    with open('input.txt') as file:
        n, m = map(int, file.readline().split())
        for i in range(n):
            graph[i + 1] = list()
        for i in range(m):
            u, v = map(int, file.readline().split())
            graph[u].append(v)
            graph[v].append(u)
        s, f = map(int, file.readline().split())

    visited = [False]
    for _ in range(n):
        visited.append(False)
    explore(s)

    with open('output.txt', 'w') as file:
        file.write(f'{"1" if visited[f] else "0"}')


print("Время работы (в секундах):", time.perf_counter()-t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Считываем данные и записываем в словарь связи между вершинами графа. Запускаем функцию explore, которая заменяет 
в каждом элементе массива visited False на True, если она может пройти из начальной точки в текущую. Если значение 
конечной точки равно True, то выводим 1, противном случае – 0.
'''

'''
4 4
1 2
3 2
4 3
1 4
1 4
Result:
1
'''

'''
4 2
1 2
3 2
1 4
Result:
0
'''
