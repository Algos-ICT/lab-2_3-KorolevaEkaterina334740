import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()

file1 = open('input.txt')
file2 = open('output.txt', 'w')
n = int(file1.readline())
sides = {}
for i in range(n):
    v1 = file1.readline()
    sides[v1] = []
    k = int(file1.readline())
    for j in range(k):
        v2 = file1.readline()
        sides[v1].append(v2)
    edge = file1.readline()
for u in sides:
    visited = []
    parent = {}
    cur_node = u
    node_found = 1
    node_completed = 0
    while True:
        visited.append(cur_node)
        flag = False
        found = False
        for i in sides[cur_node]:
            if i == u:
                file2.write('YES\n')
                found = True
                break
            if i not in visited:
                parent[i] = cur_node
                cur_node = i
                node_found += 1
                flag = True
                break
        if found:
            break
        if not flag:
            node_completed += 1
            if node_found == node_completed:
                break
            cur_node = parent[cur_node]
    if not found:
        file2.write('NO\n')


print("Время работы (в секундах):", time.perf_counter() - t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Для чтобы функция была потенциально рекурсивной, нужно, чтобы в графе существовал цикл, включающий данную функцию. 
Для этого с помощью обхода в глубину ищем из вершины графа в саму себя, как и в задаче 3.
P.s.3 задача: Считываем граф, учитывая, что он ориентированный. По сути, чтобы обнаружить цикл, нужно найти вершину, 
которая достижима сама из себя. Для пользуемся обходом в глубину и пробегаемся по всем вершинам графа. Если таковая 
вершина  находится, значит в графе есть цикл и выводится ‘1’. В обратном случае выводится ‘0’.
'''

'''
3
p1
2
p1
p2
*****
p2
1
p1
*****
p3
1
p1
*****

Result:
YES 
YES
NO
'''