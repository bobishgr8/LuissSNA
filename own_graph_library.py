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

class graph(object):
    def __init__(self):
        pass

