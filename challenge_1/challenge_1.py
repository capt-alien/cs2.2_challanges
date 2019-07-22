#!python3
import sys
from ast import literal_eval as make_tuple

from adjancy_list import Graph
# from adjancy_matrix import Graph

def graphify_text_file(filename):
    f=open(filename, "r", encoding="utf8")
    lines = f.readlines()
    f.close()
    #create Graph
    graph = Graph()
    #get rid of \n
    lines = list(map(lambda line: line.strip('\n'), lines))
    for x in range(2, len(lines)):
        lines[x] = make_tuple(lines[x])
    #Create Verticies in line
    vertices = make_tuple(lines[1])#.split(',')
    for x in vertices:
        graph.add_vertex(x)
    #Run the rest of the list through a for loop
    for y in range(2, len(lines)):
        #check len for weighted
        graph.add_weighted_edge(lines[y][0], lines[y][1], lines[y][2])

    return graph

def print_graph(graph):
    print("Number of Verticies:"+str(graph.size))
    print("Number of Edges:"+str(graph.edges))
    print("Edge list:")
    #itterate through vertexes and get edges
    edges = graph.get_edges()
    for edge in edges:
        print(edge)


if __name__ == '__main__':
    grapher = graphify_text_file(sys.argv[1])
    print_graph(grapher)
