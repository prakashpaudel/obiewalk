from graph import Graph, Edge, Node
import dijkstra

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

    start = raw_input("Where do you want to start? ")
    end = raw_input("Where do you want to end? ")
    raw_list = []

    for city in g.cityList:
        raw_list.append(city.name)

    if start in raw_list and end in raw_list:
        print dijkstra.dijkstra(g.get_city(start), g.get_city(end), g)
    else:
        if start not in raw_list:
            print "Sorry,", start, "is not a valid city name."
        else:
            print "Sorry,", end, "is not a valid city name."

main()
