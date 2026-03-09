import numpy as np
import networkx as nx

class Node(object):
    def __init__(self, index, label, movie_id):
        self.index = index
        self.label = label
        self.movie_id = movie_id
        self.links = [] # Adj. list construction
    
    def __str__(self):
        return f"index: {self.index}, label: {self.label}, movie_id {self.movie_id}, out degree {self.get_out_degree()}, out strength: {self.get_out_strenght()}"
    
    def get_out_degree(self):
        """
        Gets the out degree of a node
        """
        return len(self.links)
    
    def get_out_strenght(self):
        """
        returns the out strength of a node
        """
        return sum([edge.weight for edge in self.links])


    def get_to_nodes(self):
        """
        Returns a list of links that the current node is connected to in a tupple format
        [(node,weight),(node,weight)] 
        """
        outs = []
        for link in self.links:
            outs.append((link.target,(link.weight)))

class Edge(object):
    def __init__(self,source,target,label,movie_id,weight):
        self.source = source
        self.target = target
        self.label = label
        self.movie_id = movie_id
        self.weight = weight

    def __str__(self):
        return f"source: {self.source}, target: {self.target}, weight: {self.weight}, movie_id: {self.movie_id}, label: {self.label}"

"""
Graph class implimented here in a odd way, possible to import as well but we shall see how it goes
"""

class Graph(object):
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.adj_matrix = None # Adj. Matrix construction later, innit as None. User to add edge.

    def add_node(self, index, label, movie_id):
        index = len(self.nodes)
        node = Node(index, label, movie_id)
        self.nodes.append(node)
        return node

    def add_edge(self, source, target, label, movie_id, weight):
        edge = Edge(source, target, label, movie_id, weight)
        self.edges.append(edge)
        self.nodes[source].links.append(edge)  # link from source to target

    # refactored in from week 1
    def count_non_0(self,arr):
        count = 0
        for i in arr:
            if i > 0:
                count += 1
        return count

    # refactored in from week 1
    def get_avg_degree(self,mode="out"):
        """
        Takes in a 2D array, the adj. matrix of the graph, and returns the count of non-zeros in a row.. can be used to compute both IN and OUT degrees!!      
        """
        # TODO
        # if you are free can go an productionise this code and add custom error functions for when mode is incorrectly specfied
        # for now we will assume the user has a prefrontal cortex

        if mode == "out":
            main_matrix = self.adj_matrix
        else:
            main_matrix = np.transpose(self.adj_matrix)
        avg_output = 0
        total_nodes = len(main_matrix)
        for i in range(total_nodes):
            non_zero = self.count_non_0(main_matrix)
            avg_output += non_zero/total_nodes
        return avg_output
    

    # refrence from week 1 function
    def density_calc(self):
        edges = len(self.edges)
        nodes = len(self.nodes)
        density = edges/(nodes*(nodes-1))
        return density

    def fill_adj_list(self):
        """
        ============== DEPREICATED ==============
        Takes the graph currently full of nodes and edges, and inserts the edges to the right node. Whole edge object is inserted for ease of use later.

        Only returns False when there is an error.

        """
        for edge in self.edges:
            try:
                self.nodes[edge.source].links.append(edge)
            except Exception as exception:
                print(f"Exception {exception} occured when insertinf edge")
                return exception

    def generate_adj_matrix(self):
        """
        Takes a graph of non-empty nodes, and non empty adj lists and fills in the adj_matrix, retruns a NxN 2d python list of floats
        """
        
        if self.nodes == []:
            self.adj_matrix = []
            return "No nodes, no adj matrix"
        
        try:
            n = len(self.nodes)
            self.adj_matrix = [[0 for i in range(n)] for j in range(n)]
            for i in range(n):
                for edge in self.nodes[i].links:
                    self.adj_matrix[i][edge.target] = edge.weight
        except Exception as exception:
            return exception
        
    def export_to_networkX(self):
        """
        Converts the current graph to a NetworkX graph.
        Returns a directed graph (DiGraph) object that can be used with NetworkX functionality.
        """
        # TODO!
        # Check for if graph is directed or undirected/ weighted unweighted, and return it as a networkX graph
        adj_matrix = np.array(self.adj_matrix)
        if np.array_equal(np.transpose(adj_matrix), self.adj_matrix):
            # Undirected graph
            pass
        else:
            G = nx.DiGraph()

            # Add nodes to the NetworkX graph with node attributes
            for node in self.nodes:
                G.add_node(node.index, label=node.label, movie_id=node.movie_id)

            # Add edges to the NetworkX graph with edge attributes
            for edge in self.edges:
                G.add_edge(
                    edge.source, 
                    edge.target, 
                    weight=edge.weight, 
                    label=edge.label,
                    movie_id=edge.movie_id
                )
            
            return G
    # can refactor here a add node function that works with the

