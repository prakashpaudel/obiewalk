from graph import Graph, Edge, Node
import dijkstra

# Parses a text file to be input to Dijkstra's, etc
# The first part of the file contains nodes
# First the name of the node, then the x coord, then the y coord
# The second half of the file contains edges between nodes
# additional edge creation has to be done based on names of nodes

#Returns the Graph

def main():
    g = Graph()
    fd = open("oberlindata.txt", "r")
    
    #adding nodes from file
    currentLine = fd.readline()
    while not (currentLine == "Edges\n"): 
        content = currentLine.split()
        city = content[0]
        xcoord = float(content[1])
        ycoord = float(content[2])        
        g.add_city(Node((xcoord, ycoord), None, city))
        
        currentLine = fd.readline()
    
    #adding edges from file
    currentLine = fd.readline()
    while not (currentLine == ""):
        content = currentLine.split()
        
        city1 = content[0]
        city2 = content[1]
        g.get_city(city1).add_edge(g.get_city(city2))
        
        currentLine = fd.readline()
        
#    for c in g.cityList:
#        print "Name: " + c.get_name()
#        c.print_edges()

    print dijkstra.dijkstra(g.get_city("Keep_E"), g.get_city("Mudd_E"), g)
    return g

main()
