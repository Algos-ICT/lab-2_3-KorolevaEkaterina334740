import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


from collections import deque

def shortPath(u, v):
    global sides
    search_queue = deque()
    search_queue.append((u, 0))
    visited = []
    while search_queue:
        cur_node, path = search_queue.popleft()
        if cur_node == v:
            return path
        path += 1
        if cur_node not in visited:
            visited.append(cur_node)
            for node in sides[cur_node]:
                search_queue.append((node, path))
    return -1

with open('input.txt') as f:
    n, m = map(int, f.readline().split())
    sides = {}
    for i in range(n+1):
        sides[i] = []
    for i in range(m):
        v1, v2 = map(int, f.readline().split())
        sides[v1].append(v2)
        sides[v2].append(v1)
    u, v = map(int, f.readline().split())

result = shortPath(u, v)
print(result)


print("Время работы (в секундах):", time.perf_counter() - t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Для решения данной задачи нам понадобится обход графа в ширину. Для этого используется очередь. В очередь добавляются 
все еще не посещенные вершины, доступные из текущей, вместе с количеством ребер, которое надо пройти, чтобы достичь 
данной вершины из исходной. Считываем неориентированный граф и кладем результат функции “shortPath” в переменную 
“result”, значение которой и есть ответ.
'''

'''
4 4
1 2
4 1
2 3
3 1
2 4
Result:
2
'''

'''
5 4
5 2
1 3
3 4
1 4
3 5
Result:
-1
'''