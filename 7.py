import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


def explore(x, temp):
    visited[x] = True
    for apex in graph[x]:
        if not visited[apex]:
            if temp:
                for t in graph[apex]:
                    if t in white:
                        return False
                white.add(apex)
                if not explore(apex, False):
                    return False
            else:
                for t in graph[apex]:
                    if t in black:
                        return False
                black.add(apex)
                if not explore(apex, True):
                    return False
    return True


def DFS(graph):
    for v in graph:
        if not visited[v]:
            black.add(v)
            if not explore(v, True):
                return False
    return True


if __name__ == '__main__':
    graph = dict()
    white, black = set(), set()
    with open('input.txt') as file:
        n, m = map(int, file.readline().split())
        for i in range(n):
            graph[i + 1] = list()
        for i in range(m):
            u, v = map(int, file.readline().split())
            graph[u].append(v)
            graph[v].append(u)
    visited = [False]
    for _ in range(n):
        visited.append(False)

    with open('output.txt', 'w') as file:
        file.write(f'{DFS(graph)}')

print("Время работы (в секундах):", time.perf_counter() - t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Считываем неориентированный граф и запускаем функцию DFS (поиск в глубину), которая проходит по каждой вершине графа. 
Если вершина еще не посещалась, то функция присваивает ей черный цвет. Затем проверяется, исследована функция или нет. 
В функции explore параметрами являются вершина и True. Затем для каждой вершины, связанной с текущей, идет проверка. 
Если вершина еще не посещалась, то проверяется, имеет ли она отличный цвет от текущей. В итоге, если все имеют различный 
цвет, то выводим True, в противном случае – False.
'''

'''
4 4
1 2
4 1
2 3
3 1
Result:
0
'''

'''
5 4
5 2
4 2
3 4
1 4
Result:
1
'''