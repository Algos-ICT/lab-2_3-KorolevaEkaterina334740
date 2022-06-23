import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


with open('input.txt') as f:
    n, m = map(int, f.readline().split())
    sides = {}
    for i in range(1, n+1):
        sides[i] = []
    for i in range(m):
        v1, v2 = map(int, f.readline().split())
        sides[v1].append(v2)

for u in sides:
    visited = []
    parent = {}
    cur_node = u
    node_found = 1
    node_completed = 0
    while True:
        visited.append(cur_node)
        flag = False
        for i in sides[cur_node]:
            if i == u:
                print(1)
                exit()
            if i not in visited:
                parent[i] = cur_node
                cur_node = i
                node_found += 1
                flag = True
                break
        if not flag:
            node_completed += 1
            if node_found == node_completed:
                break
            cur_node = parent[cur_node]


print("Время работы (в секундах):", time.perf_counter() - t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Считываем граф, учитывая, что он ориентированный. По сути, чтобы обнаружить цикл, нужно найти вершину, которая
достижима сама из себя. Для пользуемся обходом в глубину и пробегаемся по всем вершинам графа. Если таковая вершина 
находится, значит в графе есть цикл и выводится ‘1’. В обратном случае выводится ‘0’.
'''

'''
4 4
1 2
4 1
2 3
3 1
Result:
1
'''

'''
5 7
1 2
2 3
1 3
3 4
1 4
2 5
3 5
Result:
0
'''