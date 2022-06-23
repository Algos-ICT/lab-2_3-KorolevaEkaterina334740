import tracemalloc
import time
t_start = time.perf_counter()
tracemalloc.start()


with open('input.txt') as f:
    N = int(f.readline())
    buses = [[] for _ in range(N+1)]
    d, v = map(int, f.readline().split())
    R = int(f.readline())
    for i in range(R):
        n1, t1, n2, t2 = map(int, f.readline().split())
        buses[n1].append((t1, n2, t2))

INF = float('inf')
Time  = [INF] * (N+1)
Time[d] = 0
visited = [False] * (N+1)
while True:
    min_time = INF
    for i in range(1, N+1):
        if not visited[i] and Time[i] < min_time:
            min_time = Time[i]
            min_village = i
    if min_time == INF:
        break
    n1 = min_village
    visited[n1] = True
    for t1, n2, t2 in buses[n1]:
        if Time[n1] <= t1 and t2 <= Time[n2]:
            Time[n2] = t2

with open('output.txt', 'w') as f:
    if Time[v] == INF:
        f.write('-1')
    else:
        f.write(str((Time[v])))


print("Время работы (в секундах):", time.perf_counter() - t_start)
print("Память %d, и пик %d" % tracemalloc.get_traced_memory())

'''
Считываем описания рейсов в массив “buses”, пункты отправления и прибытия. Далее формируем массив “Time”, который мы 
заполняем бесконечностями, а ячейку пункта отправления обнуляем. Массив будет показывать минимальное время прибытия в 
соответствующую деревню. Также понадобится массив “visited” для обозначения того, проверили ли мы все рейсы из данной 
деревни или нет. В цикле мы ищем деревню с минимальным временем прибытия и отмечаем ее, как проверенную на все рейсы. 
Затем проверяем рейсы из данной деревни. Если время его отправления из нее меньше, чем время прибытия в нее, а время 
прибытия в другую деревню меньше той, что была, то заменяем время прибытия в деревню по соответствующему рейсу. 
Таким образом, мы получим массив прибытий в деревни за минимально возможное время. Если же значение времени осталось
бесконечным, то в данную деревню невозможно попасть с данными рейсами.
'''

'''
3
1 3
4
1 0 2 5
1 1 2 3
2 3 3 5
1 1 3 10
Result:
5
'''