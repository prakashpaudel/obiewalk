from graph import Graph, Node, Edge

def dijkstra(s, e, g):
    if s.name == e.name:
        return s.name

    pred = {} # dictionary of predecessors
    dist = {} # dictionary of distances
    E = [] # set of explored nodes
    for node in g.cityList:
        pred[node.name] = None
        dist[node.name] = -50

    dist[s.name] = 0
    F = PriorityQueue()
    F.put((dist[s.name],s.name))

    while not F.empty():
        # get v, which has min dist of all UNEXPLORED vertices
        v = F.get()
        if v[1] == e.name:
            break
        E.append(v[1]) # mark v as explored
        
        node = g.get_city(v[1])
        for w in node.neighbors:
            name = w.city.name
            if (dist[v[1]] + w.dist) < dist[name]:
                pred[name] = v[1]
                dist[name] = dist[v[1]] + w.dist
                # if w not in F, add it
                F.put((name, dist[name]))

    
