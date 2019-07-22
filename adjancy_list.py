#!python3
# Code Inspired by Ansel's work.

class Graph(object):
    """Impliments a graph as a list
        of Adjancies"""

    def __init__(self):
        self.graph = {}
        self.weights = {}
        self.weighted = weighted
        self.directed = directed
        self.edges = 0

    def __repr__(self):
        return "graph({})".format(self.graph)

    @property
    def size(self):
        return len(self.graph)

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
        # self.graph[vert_2].add(vert_1)
        self.edges += 1


    def add_weighted_edge(self, vert_1, vert_2, weight=0):
        """Adds a weighted edge between two
            verticies. If no weight given it defaults to a
             weight of 0"""
        assert isinstance(weight, int), "weight is not an intiger"

        if vert_1 not in self.graph:
            self.add_vertex(vert_1)
        if vert_2 not in self.graph:
            self.add_vertex(vert_2)

        if vert_2 not in self.graph[vert_1]:
            slef.graph[vert_1].add(vert_2)
            # if the graph is weighted, store edge weights in dictionary
            self.weights[(vert_1, vert_2)] = weight

        # If the graph can go both ways, add edge going opposite way
        if self.directed is False:
            self.graph[vert_2].add(vert_1)
            self.weights[(vert_2, vert_1)] = weight

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

        def get_edges(self):
            """Returns the list of all edges and weights in the graph."""
            edge_list = set()

            for vert_1 in self.graph:
                for vert_2 in self.get_neighbors(vert_1):
                    if self.weighted:
                        weight = self.weights[(vert_1, vert_2)]

                      # If the graph is directed, as to edge list as normal
                    if self.directed and self.weighted:
                        edge_list.add((vert_1, vert_2, weight))
                    if self.directed and not self.weighted:
                        edge_list.add((vert_1, vert_2))

                                # If the graph is undirected, make sure only one edge between
                # two vertices is counted. My implementation stores a directed
                # edge from and to both vertices for easier traversals.
                    if not self.directed and self.weighted:
                        if (vert_1, vert_2, weight) not in edge_list:
                            edge_list.add((fvert_1, vert_2, weight))
                    if not self.directed and not self.weighted:
                        if (vert_1, vert_2) not in edge_list:
                            edge_list.add((vert_1, vert_2))
        return edge_list
