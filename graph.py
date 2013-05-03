## Graph data structure
# CS364 - Meg Davis, Pablo Horth, and Prakash Paudel

from math import sqrt

"""
Edge class:
Each edge has:
   - The city being connected to, stored as a node
   - The distance to that city, stored as a float
"""
class Edge:
    ## Each edge has:
    # city1, city2 - the two cities it connects
    # distance - the distance between the 2 cities
    def __init__(self, city=None, dist=0.0):
        self.city = city
        self.dist = dist

"""
Node class:
Each node has:
   - A coordinate, stored as a tuple
   - Neighbors, a list of edges
   - A name, the name of the city it represents.
"""
class Node:
    ## Each node has:
    # An (x,y) coordinate (tuple)
    # A list of its neighbors
    def __init__(self, coord=(0.0,0.0), neighbors=None, name=""):
        self.coord = coord
        self.neighbors = []
        if neighbors:
            self.neighbors.append(neighbors)
        self.name = name

    # Takes in a Node and adds it to this node's list of cities
    def add_edge(self, city):
        dist = sqrt((city.coord[0] - self.coord[0])**2 + (city.coord[1] - self.coord[1])**2)
        temp = Edge(city,dist)
        self.neighbors.append(temp)

class Graph:
    def __init__(self, cities=None, edges=None):
        # List of cities in the graph (nodes)
        # Assume that all edges have already been created for the graph?
        self.cityList = []
        if cities:
            for city in cities:
                self.cityList.append(city)

def dij(start, finish, graph):
    queue = start.neighbors 
    queue = sorted(queue, key=lambda edge: edge.dist)
    path = []
    explored = []
    while queue not empty: 
        explored.append(queue[0].city)
        # add the city to the explored set
        
        del queue[0]
    for city in cities:
        queue = []
        city.neighbors = sorted(city.neighbors, key=lambda edge: edge.dist)
        # now each cities neighbors are sorted by distance
        queue = city.neighbors
        while 
        del queue[0] # remove after exploring

# Testing creation of nodes
city1 = Node((1.0, 2.0), None, "Oberlin")
city2 = Node((1.5, 2.2), None, "Elyria")
city3 = Node((4.0, 5.2), city2, "Kipton")
city1.add_edge(city2)
city2.add_edge(city1)
city2.add_edge(city3)
city4 = Node((10.0, 20.3), city2, "Cleveland")
city2.add_edge(city4)
cities = [city1, city2, city3]
edges = city2.neighbors
for edge in sorted(edges, key=lambda edge: edge.dist):
    print edge.city.name, edge.dist
    


# TODO: File format that we can easily parse
# to set up the graph without manually entering all of them.

