class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict
        self.visited = {vertex: False for vertex in self.getVertices()}

    def getVertices(self):
        return list(self.gdict.keys())

    def getEdges(self, vertex):
        return self.gdict[vertex]

    def displayGraph(self):
        print(self.gdict)
