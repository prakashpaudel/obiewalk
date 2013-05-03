# implementation of dijkstra's
# obiewalk

from graph import Graph, Edge, Node

# start : originating node
# finish : end goal
# graph : current graph
# nodes indexed by name
def dijkstra(start, finish, graph):
    dist = {}
    pred = {}
    unexplored = []

    for city in graph.cityList:
        dist[city.name] = -1.0
        pred[city.name] = None
        unexplored.append(city.name)

    dist[start.name] = 0
    
    while len(unexplored) > 0:
        min = -50
        minName = ""
        for name in unexplored:
            if min == -50 or dist[name] < min:
                min = dist[name]
                minName = name
        
        unexplored.remove(minName) 
        city = graph.get_city(minName)

        # iterate through the edges
        for neighbor in city.neighbors:
            temp = neighbor.city.name # get city associated with edge
            if dist[temp] < dist[minName] + neighbor.dist:
                dist[temp] = dist[minName] + neighbor.dist
                pred[temp] = minName
    # The problem with this is that
    # they can loop infinitely..
    # but this might just be a problem with dijkstra's and not the implementation

    print dist
    print pred

    final_path = []
    cur = finish.name

    while cur != start.name:
        if final_path.count(cur) == 0:
            final_path.insert(0,cur)
            cur = pred[cur]
        else:
            break

    final_path.insert(0,start)

    return final_path, dist[finish.name]
