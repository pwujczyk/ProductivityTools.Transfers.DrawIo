class Vertex:


    def __init__(self, name, cushion, id):
        self.name=name
        self.cushion=cushion
        self.id=id
        self.edges=[]

    def add_edge(self, edge):
        self.edges.append(edge)