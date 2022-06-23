import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


import collections


def find_min_path(elements_graph, start: str, end: str):
    len_map = dict()
    queue_name = collections.deque()
    len_map[start] = 0
    queue_name.append(start)
    while len(queue_name) != 0:
        curr_v = queue_name.popleft()
        if curr_v == end:
            return len_map[curr_v]
        if curr_v in elements_graph:
            for next_elem in elements_graph[curr_v]:
                if next_elem not in len_map:
                    len_map[next_elem] = len_map[curr_v] + 1
                    queue_name.append(next_elem)
    return -1


if __name__ == '__main__':
    n = int(input())
    elements_graph = dict()
    for i in range(n):
        inp_str = list(map(str, input().split(" -> ")))
        if inp_str[0] not in elements_graph:
            elements_graph[inp_str[0]] = [inp_str[1]]
        else:
            elements_graph[inp_str[0]].append(inp_str[1])
    fr_element = input()
    to_elem = input()
    print(find_min_path(elements_graph, fr_element, to_elem))

print("Время работы (в секундах):", time.perf_counter() - t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Задача аналогична задаче 6, только вместо чисел, ключами вершин графа являются названия веществ. 
Поэтому делаем поправку на ввод ориентированного графа, и задача решена. 
P.s.6 задача: Для решения данной задачи нам понадобится обход графа в ширину. Для этого используется очередь. В очередь 
добавляются все еще не посещенные вершины, доступные из текущей, вместе с количеством ребер, которое надо пройти, чтобы 
достичь данной вершины из исходной. Считываем неориентированный граф и кладем результат функции “shortPath” в переменную
“result”, значение которой и есть ответ.

'''

'''
5
Aqua -> AquaVita
AquaVita -> PhilosopherStone
AquaVita -> Argentum
Argentum -> Aurum
AquaVita -> Aurum
Aqua
Aurum

Result:
2
'''

'''
5
Aqua -> AquaVita
AquaVita -> PhilosopherStone
AquaVita -> Argentum
Argentum -> Aurum
AquaVita -> Aurum
Aqua
Osmium

Result:
-1
'''