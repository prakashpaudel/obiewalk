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

    def __repr__(self):
        return self.name

    def print_edges(self):
        print "Neighbors for", self.name, ":"
        for bud in self.neighbors:
            print bud.city.name, 
        print "\n"

    # Takes in a Node and adds it to this node's list of cities
    # also adds it to the other node's list of cities, if it is not already there
    def add_edge(self, city):
        dist = sqrt((city.coord[0] - self.coord[0])**2 + (city.coord[1] - self.coord[1])**2)
        temp = Edge(city,dist)
        self.neighbors.append(temp)
        temp2 = Edge(self,dist)
        city.neighbors.append(temp2)

    # Takes in a node and checks to see if it already has it in its edge list.
    def has_edge(self, name):
        for pal in self.neighbors:
            if pal.city.name == name:
                return True
        return False

class Graph:
    def __init__(self, cities=None, edges=None):
        # List of cities in the graph (nodes)
        self.cityList = []
        if cities:
            for city in cities:
                self.cityList.append(city)

    def __repr__(self):
        ret = "Cities: "
        for city in self.cityList:
            ret = ret + city.name + " "
        return ret
    
    ## Add a node to the list of cities
    def add_city(self, city):
        self.cityList.append(city)
        
    ## Takes in the name of a city and returns true if already in graph,
    ## false otherwise.
    def has_city(self, name):
        if len(self.cityList) > 0:
            for city in self.cityList:
                if city.name == name:
                    return True
        return False

    def get_city(self,name):
        if len(self.cityList) > 0:
            for city in self.cityList:
                if city.name == name:
                    return city
        return None


