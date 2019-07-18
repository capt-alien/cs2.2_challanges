#!python3
# Code Inspired by Ansel's work.
import sys

class Graph(object):
    """Impliments a graph as a list
        of Adjancies"""

    def __init__(self):
        self.graph = {}
        self.size = 0

    def __repr__(self):
        return "graph({})".format(self.graph)

    def size(self):
        return self.size

    def add_vertex(self, vert):
        """Add a Vertex to the Graph."""
        #check to see if vertex in graph
        if vert in self.graph:
            raise KeyError("{} is already in the Graph".format(vert))
        self.graph[vert]= set()
        self.size += 1

    def add_edge(self, vert_1, vert_2):
        """Adds a direct edge between two
            verticies"""
        if vert_1 not in self.graph:
            self.add_vertex(vert_1)

        if vert_2 not in self.graph:
            self.add_vertex(vert_2)

        self.graph[vert_1].add(vert_2)


    def add_weighted_edge(self, vert_1, vert_2, weight):
        """Adds a weighted edge between two
            verticies"""
        pass

    def has_vertex(self, vert_key):
        """Find the vertex in the graph named vert_key
            and if it exists returns True."""
        if vert_key not in self.graph:
            return False
        return True

    def get_vertices(self):
        """Retunrn the list of all verticies in the graph."""
        verticies = [vertex for vertex in self.graph.keys()]
        return verticies

    def get_neighbors(self, vert):
        """Lasts all vertices y such that there is an
            edge from the vert to the vertex y"""
        if vert not in self.graph:
            raise KeyError("Vertex {} is not in the graph")
        return self.graph[vert]


def graphify_text_file(filename):
    f=open(filename, "r", encoding="utf8")
    lines = f.readlines()
    f.close()
    #create Graph
    graph = Graph()
    #Create Verticies in line 2
    vertices = lines[1][0:-1].split(',')
    for x in vertices:
        graph.add_vertex(x)
    #Run the rest of the list through a for loop




if __name__ == '__main__':
    graphify_text_file(sys.argv[1])
