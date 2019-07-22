#!python3
# Code Inspired by Ansel's work.
import sys
from ast import literal_eval as make_tuple

class Graph(object):
    """Impliments a graph as a list
        of Adjancies"""

    def __init__(self):
        self.name_to_index = {}
        self.index_to_name = {}
        self.graph = []
        self.edge_list = []

    def __repr__(self):
        return "graph({})".format(self.graph)

    @property
    def size(self):
        return len(self.graph)

    def add_vertex(self, vert):
        """Add a Vertex to the Graph."""
        #check to see if vertex in graph
        if vert in self.name_to_index:
            raise KeyError("{} is already in the Graph".format(vert))

        self.name_to_index[vert] = self.size
        self.index_to_name[self.size] = vert

        for row in self.graph:
            row.append(0)

        # Because vertex has not been added yet, range should account for
        # missing vertex with a +1
        self.graph.append([0 for vertex in range(self.size + 1)])

    def add_edge(self, vert_1, vert_2):
        """Adds a direct edge between two
            verticies"""
        if vert_1 not in self.name_to_index:
            self.add_vertex(vert_1)

        if vert_2 not in self.name_to_index:
            self.add_vertex(vert_2)

        vert_1_index = self.name_to_index[vert_1]
        vert_2_index = self.name_to_index[vert_2]

        self.graph[vert_1_index][vert_2_index] = 1

        if self.graph[vert_1_index][vert_2_index] != 1:
            self.graph[vert_1_index][vert_2_index] = -1

        self.edge_list.append((vert_1, vert_2))

    def add_weighted_edge(self, vert_1, vert_2, weight):
        """Adds a weighted edge between two
            verticies"""
        pass

    def has_vertex(self, vert_key):
        """Find the vertex in the graph named vert_key
            and if it exists returns True."""
        if vert_key not in self.name_to_index:
            return False
        return True

    def get_vertices(self):
        """Retunrn the list of all verticies in the graph."""
        return [vertex for vertex in self.name_to_index.keys()]

    def get_neighbors(self, vert):
        """Lasts all vertices y such that there is an
            edge from the vert to the vertex y"""
        if vert not in self.name_to_index:
            raise KeyError("{} vertex is not in graph".format(vert))

        vert_index = self.name_to_index[vert]
        neighbors = set()

        for index, edge in enumerate(self.graph[vert_index]):
            if edge == 1:
                neighbors.add(self.index_to_name[index])

        return neighbors
