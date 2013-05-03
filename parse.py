from graph import Graph, Edge, Node


# Parses a text file to be input to Dijkstra's, etc
# Each line contains a new node
# First the name of the node, then the x coord, then the y coord
# and finally a variable number of edges
def main():
    g = Graph()
    fd = open("test.txt", "r")

    for line in fd: 
        content = line.split()

        city = content[0]
        xcoord = float(content[1])
        ycoord = float(content[2])
        
        temp = Node((xcoord, ycoord), None, city)
        # get the edges
        edgelist = []
        for i in range(3,len(content)):
            edgelist.append(content[i])
        for val in edgelist:
            if g.has_city(val):
                buddy = g.get_city(val)
                temp.add_edge(buddy)

        g.add_city(temp)

    for city in g.cityList:
        if city.has_edge("Hamilton"):
            print "Yeah!"
        else:
            print "Nah!"
        
main()
