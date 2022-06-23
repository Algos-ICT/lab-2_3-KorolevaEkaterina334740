import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


def extractMin():
    m = float('+inf')
    im = 0
    for i in graph:
        if distance[i] < m:
            m = distance[i]
            im = i
    if im == 0:
        return im, []
    subj = graph[im]
    graph.pop(im)
    return im, subj


def dijkstra(start):
    distance[start] = 0
    while len(graph) != 0:
        u, subj = extractMin()
        if u == 0:
            break
        for v in subj:
            if distance[v] > distance[u] + weights[(u, v)]:
                distance[v] = distance[u] + weights[(u, v)]


if __name__ == '__main__':
    graph = dict()
    weights = dict()
    distance = [float('+inf')]
    with open('input.txt') as file:
        n, m = map(int, file.readline().split())
        for i in range(n):
            graph[i + 1] = list()
        for i in range(m):
            u, v, m = map(int, file.readline().split())
            graph[u].append(v)
            weights[(u, v)] = m
        s, f = map(int, file.readline().split())

    for _ in range(n):
        distance.append(float('+inf'))

    dijkstra(s)

    with open('output.txt', 'w') as file:
        file.write(f'{"-1" if distance[f] == float("+inf") else str(distance[f])}')

print("Время работы (в секундах):", time.perf_counter() - t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Считываем входные данные, записываем веса в значения отдельного словаря, в котором ключи – ребра. Затем запускаем 
алгоритм Дейкстры. В этом алгоритме мы проходим по каждому значению графа, запуская функцию extractMin, которая находит 
минимальный вес из всех возможных, записывая его индекс. Затем из основного графа удаляется вершина с этим весом и 
значения индекса и подграфа возвращаются в алгоритм Дейкстры. Затем проверяется, если хоть одна из вершин подграфа имеет 
большую дистанцию, чем дистанция полученного индекса и вес ребра, то заменяем. В итоге получаем минимальный вес, 
в противном случае – -1.
'''

'''
4 4
1 2 1
4 1 2
2 3 2
1 3 5
1 3
Result:
3
'''

'''
5 9
1 2 4
1 3 2
2 3 2
3 2 1
2 4 2
3 5 4
5 4 1
2 5 3
3 4 4
1 5
Result:
6
'''

'''
3 3
1 2 7
1 3 5
2 3 2
3 2
Result:
-1
'''