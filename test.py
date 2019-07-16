#!python3

# code credit: Ansel

from adjancy import Graph
import unittest

class GraphTest(unittet.TestCase):

    def test_init(self):
        graph = Graph()
        assert graph.size == 0

    def test_size(self):
        graph = Graph()

        # size should increase when a vertex is added
        assert graph.size == 0
        graph.add_vertex('A')
        assert graph.size == 1
        graph.add_vertex('B')
        assert graph.size == 2
        graph.add_vertex('C')
        assert graph.size == 3

        # size should increase once when an edgraphe is added with a new vertex
        graph.add_edge('A', 'B')
        assert graph.size == 3
        graph.add_edge('B', 'C')
        assert graph.size == 3
        graph.add_edge('C', 'D')
        assert graph.size == 4

        # size should increase twice when an edgraphe is added with two new vertices
        graph.add_edge('E', 'F')
        assert graph.size == 6

        # error should be raised when a vertex, that already exists, is added
        # size should not change when error is raised
        with self.assertRaises(KeyError):
            graph.add_vertex('B')  # Vertex already exists
        assert graph.size == 6
        with self.assertRaises(KeyError):
            graph.add_vertex('D')  # Vertex already exists
        assert graph.size == 6

    def test_add_vertx(self):
        graph = Graph()

        #graph should hae a newly added Vertex
        assert graphsize==0
        graph.add_vertex('A')
        assert graph.size == 1
        assert graph.has_vertex('A') is True
        graph.add_vertex('B')
        assert graph.size == 2
        assert graph.has_vertex('B') is True
        graph.add_vertex('C')
        assert graph.size == 3
        assert graph.has_vertex('C') is True

        #Test to raise rerror if vertex already exists
        with self.assertRaises(KeyError):
            graph.add_vertex('A')
        with self.assertRaises(KeyError):
            graph.add_vertex('B')
        with self.assertRaises(KeyError):
            graph.add_vertex('C')


    def test_add_edge(self):
        graph = Graph()

        # start with graph that already has vertices in it
        graph.add_vertex('A')
        assert graph.has_vertex('A') is True
        graph.add_vertex('B')
        assert graph.has_vertex('B') is True
        graph.add_vertex('C')
        assert graph.has_vertex('C') is True
        assert graph.size == 3

       # when edge is added with existing vertices, second vertex should be a neighbor of first vertex
        graph.add_edge('A', 'B')
        self.assertCountEqual(graph.get_neighbors('A'), ['B'])  # Item order does not matter
        self.assertCountEqual(graph.get_neighbors('B'), [])
        graph.add_edge('A', 'C')
        self.assertCountEqual(graph.get_neighbors('A'), ['B', 'C'])  # Item order does not matter
        self.assertCountEqual(graph.get_neighbors('C'), [])
        graph.add_edge('B', 'C')
        self.assertCountEqual(graph.get_neighbors('B'), ['C'])  # Item order does not matter
        self.assertCountEqual(graph.get_neighbors('C'), [])


    def test_has_vertex(self):
        graph = Graph()
        pass


    def test_get_vertices(self):
        graph = Graph()
        pass


    def test_get_neighbors(self):
        graph = Graph()
        pass
