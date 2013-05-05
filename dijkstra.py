# dijkstra's

from graph import Graph, Edge, Node
import heapq

# start : originating node
# finish : end goal
# graph : current graph
# nodes indexed by name
def dijkstra(start, finish, graph):
    pq = []
    dist, pred = {}, {}
    explored = [start.name] 

    # init values to something
    for node in graph.cityList:
        dist[node.name], pred[node.name] = -1, None

    dist[start.name] = 0   
    
    # initialize PQ to contain s's edges
    for edge in start.neighbors:
        node = edge.city
        dist[node.name] = edge.dist
        # push onto the heap: [dist, node, parent]
        heapq.heappush(pq, [dist[node.name], node.name, start.name])

    # While there are items in the priority queue...
    while pq:
        # let next be the min element of pq
        edge_cost, next, p = heapq.heappop(pq)
        
        if next == finish.name:
            pred[next] = p
            break

        if next not in explored:
            explored.append(next)
            pred[next] = p
            node = graph.get_city(next)
            for edge in node.neighbors:
                city = edge.city.name
                if dist[city] != -1:
                    # if the current distance entry is greater than the updated one, update it.
                    if dist[city] > edge.dist + dist[next]: # next = parent, city = edge we are exploring now
                        dist[city] = edge.dist + dist[next]
                        # decrease the key, update dist & predecessor
                        heapq._siftdown(pq, 0, pq.index([dist[city], city, next]))
                else:
                    dist[city] = edge.dist + dist[next]
                    heapq.heappush(pq, [dist[city], city, next])

    # build the list
    cur, path = finish.name, []
    while pred.get(cur):
        path.insert(0, pred.get(cur))
        cur = pred[cur]       

    path.append(finish.name)

    return path
