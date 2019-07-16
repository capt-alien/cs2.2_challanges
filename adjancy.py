#! python3
# Code Inspired by Ansel's work.

class Graph(object):
    """Impliments a graph as a list
        of Adjancies"""

    def __init__(self):
        pass

    def __repr__(self):
        pass

    @property
    def size(self):
        pass

    def add_vertex(self, vert):
        """Add a Vertex to the Graph."""
        pass

    def add_edge(self, vert_1, vert_2):
        """Adds a direct edge between two
            verticies"""
        pass

    def add_weighted_edge(self, vert_1, vert_2, weight):
        """Adds a weighted edge between two
            verticies"""
        pass

    def has_vertex(self, vert_key):
        """Find the vertex in the graph named vert_key
            and if it exists returns True."""
        pass

    def get_verticies(self):
        """Retunrn the list of all verticies in the graph."""
        pass

    def get_neighbors(self, vert):
        """Lasts all vertices y such that there is an
            edge from the vert to the vertex y"""
        pass
