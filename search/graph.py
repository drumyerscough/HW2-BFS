import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        A method that performs a breadth first traversal and pathfinding

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        
        # check edge cases where start and end nodes are not in the graph
        if start not in self.graph:
            raise Exception('The start node is not in the graph')
        elif end != None and end not in self.graph:
            raise Exception('The end node is not in the graph')

        # initialize the queue, list of visited nodes, and a mapping of nodes to their parents in the BFS traversal
        queue = [start]
        visited = [start]
        parents = {start: None}

        # do BFS
        while len(queue) > 0:
            v = queue.pop(0)
            for nbr in self.graph.successors(v):
                if nbr not in visited:
                    visited.append(nbr)
                    queue.append(nbr)
                    parents[nbr] = v

        # if no end node is provided, return the BFS ordering
        if end == None:
            return visited
        
        # if an end node is provided and it was visited, return the shortest path
        elif end != None and end in visited:
            path = []
            v = end
            while v != None:
                path.append(v)
                v = parents[v]
            return path
        
        # if an end node is provided but wasn't visited, return None
        else:
            return None
        




