# implementation of dijkstra's
# obiewalk

from graph import Graph, Edge, Node
import heapq


# start : originating node
# finish : end goal
# graph : current graph
# nodes indexed by name
def dijkstra(start, finish, graph):
    pq = []     # priority queue of items to explore, implemented using heapq
    dist, pred, track = {}, {}, {}
    explored = [start.name] # create the explored set

    # init values to something
    for node in graph.cityList:
        dist[node.name], pred[node.name] = -1, None

    dist[start.name] = 0    # set starting distance to 0
    
    # Itemized entries are stored in the series: 
    # [next, parent, edge_cost]

    # initialize PQ to contain s's edges 
    # we're doing this by edge
    for edge in start.neighbors:
        node = edge.city
        dist[node.name] = edge.dist
        track[node.name] = [node.name, start.name, dist[node.name]] # add info to track dict
        heapq.heappush(pq, [node.name, start.name, dist[node.name]]) # push onto the priority queue

    # While there are items in the priority queue...
    while pq:
        # let next be the min element of pq
        next, p, edge_cost = heapq.heappop(pq)

        if next == finish.name:
            pred[next] = p # add pred, else the last while loop will not work
            break

        if next not in explored:
            explored.append(next)
            pred[next] = p
            node = graph.get_city(next)
            for edge in node.neighbors:
                city = edge.city.name
                if dist[city] != -1:
                    # if the current distance entry is greater than the updated one, update it.
                    if dist[city] > edge.dist + dist[next]:
                        dist[city] = edge.dist + dist[next]
                        # decrease the key
                        track[city][2] = dist[city] # update the queue too
                        track[city][1] = next
                        heapq._siftdown(pq, 0, pq.index(track[city]))
                else:
                    dist[city] = edge.dist + dist[next]
                    heapq.heappush(pq, [city, next, dist[city]])
                    track[city] = [city,next,dist[city]]

    cur = finish.name
    path = []

    while pred.get(cur):
        path.insert(0, pred.get(cur))
        cur = pred[cur]       
    path.append(finish.name)

    return path
