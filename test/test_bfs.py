# write tests for bfs
import pytest
from search import graph
import networkx as nx

def test_bfs_traversal():
    """
    Tests to make sure that the BFS method correctly returns a
    BFS ordering starting from a selected node. This test reads
    in the 'tiny_network.adjlist' graph and compares the length and
    ordering to those obtained using the corresponding networkx 
    function.
    """
    g = graph.Graph('data/tiny_network.adjlist')
    my_bfs = g.bfs('Nevan Krogan')
    nx_bfs = list(nx.bfs_tree(g.graph, 'Nevan Krogan').nodes()) 

    # check that the correct number of nodes were found by each search
    assert len(my_bfs) == len(nx_bfs)

    # check that the nodes were returned in the same order
    assert my_bfs == nx_bfs


def test_bfs():
    """
    Tests to make sure that the BFS method correctly returns a
    shortest path between nodes that are connected and does not
    return a path for nodes that are not connected. This test reads
    in the 'citation_network.adjlist' graph and compares the paths
    (or absence thereof) to those obtained using the corresponding
    networkx functions until 50 pairs of reachable nodes and 50 pairs
    of unreachable nodes have been tested.
    """
    g = graph.Graph('data/citation_network.adjlist')

    # so that this test finishes in a reasonable amount of time, limit to 50
    limit = 50
    has_path_counter = 0
    no_path_counter = 0

    for node1 in g.graph.nodes():
        for node2 in g.graph.nodes():
            if node1 != node2 and (has_path_counter < limit or no_path_counter < limit):
                my_bfs = g.bfs(node1, end=node2)
                
                # if the nodes are connected, check that my bfs implementation returns one
                # of the shortest paths
                if nx.has_path(g.graph, node1, node2):
                    if has_path_counter < limit:
                        assert my_bfs[::-1] in list(nx.all_shortest_paths(g.graph, source=node1, target=node2))
                        has_path_counter += 1

                # if the nodes are not connected, check that my bfs implementation returns None
                else:
                    if no_path_counter < limit:
                        assert my_bfs == None
                        no_path_counter += 1


def test_bfs_exceptions():
    """
    Tests to make sure that my BFS implementation raises exceptions
    and does not run when given bad inputs, e.g. nodes that aren't in
    the graph.
    """
    g = graph.Graph('data/citation_network.adjlist')

    # check that an exception is raised if the start node is not in the graph
    with pytest.raises(Exception):
        my_bfs = g.bfs('Dru Myerscough')

    # check that an exception is raised if the emd node is not in the graph
    with pytest.raises(Exception):
        my_bfs = g.bfs('Nevan Krogan', end='Dru Myerscough')