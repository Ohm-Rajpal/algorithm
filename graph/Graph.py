class Graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict


    def getVertices(self):
        return list(self.gdict.keys())