#!python3

# code credit: Ansel

from graph import Graph
import unittest

class GraphTest(unittest.TestCase):

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

    def test_add_vertex(self):
        graph = Graph()

        #graph should hae a newly added Vertex
        assert graph.size==0
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

        print(graph.graph)

       # when edge is added with existing vertices, second vertex
       # should be a neighbor of first vertex
        graph.add_edge('A', 'B')
        self.assertCountEqual(graph.get_neighbors('A'), ['B'])
        self.assertCountEqual(graph.get_neighbors('B'), [])
        graph.add_edge('A', 'C')
        self.assertCountEqual(graph.get_neighbors('A'), ['B', 'C'])
        self.assertCountEqual(graph.get_neighbors('C'), [])
        graph.add_edge('B', 'C')
        self.assertCountEqual(graph.get_neighbors('B'), ['C'])
        self.assertCountEqual(graph.get_neighbors('C'), [])

        # when edge is added with nonexistent vertices, add nonexistent vertices
        # then, second vertex should be a neighbor of first vertex
        graph.add_edge('B', 'D')
        self.assertCountEqual(graph.get_neighbors('B'), ['C', 'D'])
        self.assertCountEqual(graph.get_neighbors('D'), [])
        graph.add_edge('E', 'F')
        self.assertCountEqual(graph.get_neighbors('E'), ['F'])
        self.assertCountEqual(graph.get_neighbors('F'), [])

        # when duplicate edge is added, the duplicate edge should be ignored
        graph.add_edge('A', 'C')
        self.assertCountEqual(graph.get_neighbors('A'), ['B', 'C'])
        self.assertCountEqual(graph.get_neighbors('C'), [])
        graph.add_edge('E', 'F')
        self.assertCountEqual(graph.get_neighbors('E'), ['F'])
        self.assertCountEqual(graph.get_neighbors('F'), [])


    def test_has_vertex(self):
        graph = Graph()

        # has_vertex should return false if vertex not in graph
        # has_vertex should return true if vertex added through add_vertex
        assert graph.has_vertex('A') is False
        graph.add_vertex('A')
        assert graph.has_vertex('A') is True
        assert graph.has_vertex('B') is False
        graph.add_vertex('B')
        assert graph.has_vertex('B') is True
        assert graph.has_vertex('C') is False
        graph.add_vertex('C')
        assert graph.has_vertex('C') is True

        # has_vertex should return true if vertex added through add_edge
        assert graph.has_vertex('D') is False
        assert graph.has_vertex('E') is False
        graph.add_edge('D', 'E')
        assert graph.has_vertex('D') is True
        assert graph.has_vertex('E') is True


    def test_get_vertices(self):
        graph = Graph()

        # get_vertices should return all vertices added by add_vertex
        assert graph.has_vertex('A') is False
        graph.add_vertex('A')
        self.assertCountEqual(graph.get_vertices(), ['A'])
        assert graph.has_vertex('B') is False
        graph.add_vertex('B')
        self.assertCountEqual(graph.get_vertices(), ['A', 'B'])
        assert graph.has_vertex('C') is False
        graph.add_vertex('C')
        self.assertCountEqual(graph.get_vertices(), ['A', 'B', 'C'])

        # get_vertices should return all vertices added by add_edge
        assert graph.has_vertex('D') is False
        assert graph.has_vertex('E') is False
        graph.add_edge('D', 'E')
        self.assertCountEqual(graph.get_vertices(), ['A', 'B', 'C', 'D', 'E'])


    def test_get_neighbors(self):
        graph = Graph()

        # neighbors should return all vertices that a given vertex directs to
        # neighbors should not return any vertices that direct to a given vertex
        graph.add_vertex('A')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_edge('A', 'B')
        self.assertCountEqual(graph.get_neighbors('A'), ['B'])
        self.assertCountEqual(graph.get_neighbors('B'), [])
        graph.add_edge('A', 'C')
        self.assertCountEqual(graph.get_neighbors('A'), ['B', 'C'])
        self.assertCountEqual(graph.get_neighbors('C'), [])


        # neighbors can return any vertices that direct to a given vertex,
        # if that vertex directs back as well
        graph.add_edge('C', 'A')
        self.assertCountEqual(graph.get_neighbors('C'), ['A'])
        graph.add_edge('C', 'B')
        self.assertCountEqual(graph.get_neighbors('C'), ['A', 'B'])


        # neighbor should still be added even if vertex is added through add_edge
        graph.add_edge('A', 'D')
        self.assertCountEqual(graph.get_neighbors('A'), ['B', 'C', 'D'])  # Item order does not matter
        self.assertCountEqual(graph.get_neighbors('D'), [])  # Item order does not matter

        # error should be raised when key is not in graph
        with self.assertRaises(KeyError):
            graph.get_neighbors('E')  # Vertex does not exist
        with self.assertRaises(KeyError):
            graph.get_neighbors('F')  # Vertex does not exist

    def test_breadth_first_search(self):
        graph = Graph()

        # Create verties and edges
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "A")
        graph.add_edge("B", "E")
        graph.add_edge("C", "D")
        graph.add_edge("D", "F")
        graph.add_edge("E", "H")
        graph.add_edge("F", "G")
        graph.add_edge("G", "H")
        graph.add_edge("H", "I")
        graph.add_edge("H", "J")
        graph.add_edge("H", "G")
        graph.add_edge("J", "B")

        # Get all vertices accessible at level 1
        level_1 = graph.breadth_first_search(v_a, 1, only_new=False)
        self.assertCountEqual(level_1, [v_b, v_c])
        # Get all vertices accessible at level 2
        level_2 = graph.breadth_first_search(v_a, 2, only_new=False)
        self.assertCountEqual(level_2, [v_a, v_d, v_e])
        # Get all vertices accessible at level 3
        level_3 = graph.breadth_first_search(v_a, 3, only_new=False)
        self.assertCountEqual(level_3, [v_b, v_c, v_f, v_h])
        # Get all vertices accessible at level 4
        level_4 = graph.breadth_first_search(v_a, 4, only_new=False)
        self.assertCountEqual(level_4, [v_a, v_d, v_e, v_g, v_i, v_j])
        # Get all vertices accessible at level 5
        level_5 = graph.breadth_first_search(v_a, 5, only_new=False)
        self.assertCountEqual(level_5, [v_b, v_c, v_f, v_h])

        # Get new vertices accessible at level 1
        new_level_1 = graph.breadth_first_search(v_a, 1)
        self.assertCountEqual(new_level_1, [v_b, v_c])
        # Get new vertices accessible at level 2
        new_level_2 = graph.breadth_first_search(v_a, 2)
        self.assertCountEqual(new_level_2, [v_d, v_e])
        # Get new vertices accessible at level 3
        new_level_3 = graph.breadth_first_search(v_a, 3)
        self.assertCountEqual(new_level_3, [v_f, v_h])
        # Get new vertices accessible at level 4
        new_level_4 = graph.breadth_first_search(v_a, 4)
        self.assertCountEqual(new_level_4, [v_g, v_i, v_j])
        # No new vertices accessible at level 5
        new_level_5 = graph.breadth_first_search(v_a, 5)
        self.assertCountEqual(new_level_5, [])

                # Test starting from vertex "g"
        # Get all vertices accessible at level 1
        graph_level_1 = graph.breadth_first_search(v_g, 1, only_new=False)
        self.assertCountEqual(graph_level_1, [v_h])
        # Get new vertices accessible at level 2
        graph_new_level_2 = graph.breadth_first_search(v_g, 2)
        self.assertCountEqual(graph_new_level_2, [v_i, v_j])
        # Get all vertices accessible at level 3
        graph_level_3 = graph.breadth_first_search(v_g, 3, only_new=False)
        self.assertCountEqual(graph_level_3, [v_b, v_h])
        # Get new vertices accessible at level 4
        graph_new_level_4 = graph.breadth_first_search(v_g, 4)
        self.assertCountEqual(graph_new_level_4, [v_a, v_e])
        # Get new vertices accessible at level 5
        graph_new_level_5 = graph.breadth_first_search(v_g, 5)
        self.assertCountEqual(graph_new_level_5, [v_c])
        # Get new vertices accessible at level 6
        graph_new_level_6 = graph.breadth_first_search(v_g, 6)
        self.assertCountEqual(graph_new_level_6, [v_d])
        # Get new vertices accessible at level 7
        graph_new_level_7 = graph.breadth_first_search(v_g, 7)
        self.assertCountEqual(graph_new_level_7, [v_f])
        # No new vertices accessible at level 8
        graph_new_level_8 = graph.breadth_first_search(v_g, 8)
        self.assertCountEqual(graph_new_level_8, [])

        # Error should be raised if passing key rather than vertex object
        with self.assertRaises(TypeError):
            graph.breadth_first_search("A", 1, only_new=False)
        with self.assertRaises(TypeError):
            graph.breadth_first_search("G", 2)
        # Error should be raised when vertex not in graph
        v_y = Vertex("Y")
        with self.assertRaises(ValueError):
            graph.breadth_first_search(v_y, 2, only_new=False)
        v_z = Vertex("Z")
        with self.assertRaises(ValueError):
            graph.breadth_first_search(v_z, 1)

    def test_shortest_path(self):
        graph = Graph()

        # Create verties and edges
        graph.add_edge("A", "B")
        graph.add_edge("A", "C")
        graph.add_edge("B", "A")
        graph.add_edge("B", "E")
        graph.add_edge("C", "D")
        graph.add_edge("D", "F")
        graph.add_edge("E", "H")
        graph.add_edge("F", "G")
        graph.add_edge("G", "H")
        graph.add_edge("H", "I")
        graph.add_edge("H", "J")
        graph.add_edge("H", "G")
        graph.add_edge("J", "B")
        # Add vertices that cannot be reached by other vertices
        graph.add_vertex('X')
        graph.add_edge("Y", "Z")

        # Find shortest path 2 edges away
        path_2 = graph.shortest_path("A", "E")
        self.assertEqual(path_2, [v_a, v_b, v_e])  # Order matters
        # Find shortest path 4 edges away
        path_4 = graph.shortest_path("A", "I")
        self.assertEqual(path_4, [v_a, v_b, v_e, v_h, v_i])  # Order matters
        # Find shortest path 7 edges away
        path_7 = graph.shortest_path("G", "F")
        true_path_7 = [v_g, v_h, v_j, v_b, v_a, v_c, v_d, v_f]  # Order matters
        self.assertEqual(path_7, true_path_7)

        # There is no shortest path between unconnected vertices in same graph
        no_path_1 = graph.shortest_path("G", "X")
        self.assertEqual(no_path_1, None)
        no_path_2 = graph.shortest_path("X", "Z")
        self.assertEqual(no_path_2, None)
        # There is no way to traverse to the same vertex
        same_vert_path = graph.shortest_path("A", "A")
        self.assertEqual(same_vert_path, None)

        # No path to vertex that does not have an edge directed into it
        graph.directed = True
        # Added directed edge from 0 to A
        graph.add_edge(0, "A")
        # Try to get 0 from A
        no_directed_path = graph.shortest_path("A", 0)
        self.assertEqual(no_directed_path, None)

        # Error should be raised when vertex not in graph
        with self.assertRaises(KeyError):
            graph.shortest_path("A", 1)
        with self.assertRaises(KeyError):
            graph.shortest_path("T", "A")


if __name__ == '__main__':
    unittest.main()
