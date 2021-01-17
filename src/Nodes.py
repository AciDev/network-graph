from itertools import chain


class Nodes(object):
    """
    A simple class to create network nodes
    """

    def __init__(self, initialNodes):
        self.nodes = list()
        self.node_number = self.__processNodes(initialNodes)
        self.__generateList(initialNodes)

    def __processNodes(self, nodes):
        highest = 0
        for n in chain.from_iterable(nodes):
            if n > highest:
                highest = n
        return highest

    def __generateList(self, nodes):
        for i in range(self.node_number):
            self.nodes.append(list())
            for j in range(self.node_number):
                con = (i+1, j+1)
                if con in nodes:
                    self.nodes[i].append(1)
                else:
                    self.nodes[i].append(0)

    def getConnections(self):
        for i, n in enumerate(self.nodes):
            connections = [j for j in range(len(n)) if n[j] == 1]
            if len(connections) > 0:
                for con in connections:
                    print(f'Node {i+1} is connected to {con+1}')
