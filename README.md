! [BuildStatus] (https://github.com/drumyerscough/HW2-BFS/workflows/HW2-BFS/badge.svg?event=push)

# Assignment 2
Breadth-first search

# Assignment Overview
The purpose of this assignment is to get you comfortable working with graph structures and to implement a breadth-first search function to traverse the graph and find the shortest path between nodes.

# Assignment Tasks

## Coding Assessment

## Software Development Assessment

This repo contains a module called search, which includes a Graph class that is wrapper for a networkx directed graph and has a method that implements breadth-first search (BFS), with options to return a BFS ordering of all nodes that are reachable from the start node or a shortest path between two nodes, if one exists. BFS is implemented as such:
* Initialize a queue, a list to hold visited nodes, and a dictionary to hold parent:child mappings from the search.
* While the queue contains at least one node, pop a node from the queue and iterate over its neighbors. For each neighbor that has not been visited, add the neighbor to the queue, the visited list, and the parents mapping (with the neighbor as the key and its parent as the value). 
* If an end node was provided in the arguments for the BFS method and was found in the search, return the path from start node to end node by iterating through the parents mapping. This path may not be unique. If the end node was not found, return None. If no end node was specified, return a BFS ordering of the nodes from the visited list. This ordering may also not be unique.

# Getting Started
To get started you will need to fork this repository onto your own github. You will then work on the code base from your own repo and make changes to it in the form of commits. 

# Reference Information
## Test Data
Two networks have been provided in an adjacency list format readable by [networkx](https://networkx.org/), is a commonly used python package for working with graph structures. These networks consist of two types of nodes:
* Faculty nodes 
* Pubmed ID nodes

However, since these are both stored as strings, you can treat them as equivalent nodes when traversing the graph. The first graph ("citation_network.adjlist") has nodes consisting of all BMI faculty members, the top 100 Pubmed papers *cited by* faculty, and the top 100 papers that *cite* faculty publications. Edges are directed and and edge from node A -> B indicates that node A *is cited by* node B. There are 5120 nodes and 9247 edges in this network.

The second network is a subgraph of the first, consisting of only the nodes and edges along the paths between a small subset of faculty. There are 30 nodes and 64 edges.

# Completing the assignment
Make sure to push all your code to github, ensure that your unit tests are correct, and submit a link to your github through the google classroom assignment.

# Grading

## Code (6 points)
* Breadth-first traversal works correctly (3)
* Traces the path from one faculty to another (2)
* Handles edge cases (1)

## Unit tests (3 points)
* Output traversal for mini data set (1)
* Tests for at least two possible edge cases (1)
* Correctly uses exceptions (1)

## Style (1 points)
* Readable code with clear comments and method descriptions
* Updated README with description of your methods

