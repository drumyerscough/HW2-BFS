# write tests for bfs
import pytest
from search import graph
import networkx as nx

def test_bfs_traversal():
    """
    Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    g = graph.Graph('tiny_network.adjlist')
    my_bfs = g.bfs('Nevan Krogan')
    nx_bfs = list(nx.bfs_tree(g.graph, 'Nevan Krogan').nodes()) 

    # check that the correct number of nodes were found by each search
    assert len(my_bfs) == len(nx_bfs)

    # check that the nodes were returned in the same order
    assert my_bfs == nx_bfs


def test_bfs():
    """
    Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    g = graph.Graph('citation_network.adjlist')

    for node1 in g.graph.nodes():
        for node2 in g.graph.nodes():
            if node1 != node2:
                my_bfs = g.bfs(node1, end=node2)
                
                # if the nodes are connected, check that my bfs implementation returns one
                # of the shortest paths
                if nx.has_path(node1, node2):
                    assert my_bfs in set(nx.all_shortest_paths(g.graph))

                # if the nodes are not connected, check that my bfs implementation returns None
                else:
                    assert my_bfs == None


def test_bfs_exceptions():
    """
    Tests to make sure that my BFS implementation raises exceptions
    and does not run when given bad inputs, e.g. nodes that aren't in
    the graph.
    """
    g = graph.Graph('citation_network.adjlist')

    # check that an exception is raised if the start node is not in the graph
    with pytest.raises(Exception):
        my_bfs = g.bfs('Dru Myerscough')

    # check that an exception is raised if the emd node is not in the graph
    with pytest.raises(Exception):
        my_bfs = g.bfs('Nevan Krogan', end='Dru Myerscough')