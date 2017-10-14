"""
utils package is for some quick utility methods

such as parsing
"""
from io import open
from .graph import Edge
from .graph import Node


class Tile(object):
    """Node represents basic unit of graph"""
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)
    def __repr__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.symbol == other.symbol
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self.x) + "," + str(self.y) + self.symbol)



def parse_grid_file(graph, file_path):
    """
    ParseGridFile parses the grid file implementation from the file path line
    by line and construct the nodes & edges to be added to graph

    Returns graph object
    """
    # TODO: read the filepath line by line to construct nodes & edges

    # TODO: for each node/edge above, add it to graph

    file = open(file_path)

    file_list = []
    for f in file:
        if f.strip() != '':
            list.append(list(f.strip())) 

    file.close()

    grid = []
    row_num = len(file_list)

    if row_num > 0:
        for i in range(1, row_num - 1):
            y = i - 1
            col = len(file_list[i])
            if col > 2:
                grid.append([])
                for j in range(1, col - 1, 2):
                    x = int((j - 1)/2)
                    tile = file_list[i][j] + file_list[i][j + 1]
                    if not tile.__eq__('##'):
                        grid[y].append(Node(Tile(x, y, str(tile))))
                    else:
                        grid[y].append(None)

        for x in range(0, len(grid)):
            for y in range(0 , len(grid[x])):
                if node_grid[x][y] is not None:
                    graph.add_node(grid[x][y])
                    if x > 0 and grid[x - 1][y] is not None:
                        graph.add_edge(Edge(grid[x - 1][y], grid[x][y], 1))
                        graph.add_edge(Edge(grid[x][y], grid[x - 1][y], 1))
                    if y > 0 and grid[x][y - 1] is not None:
                        graph.add_edge(Edge(grid[x][y - 1], grid[x][y], 1))
                        graph.add_edge(Edge(grid[x][y], grid[x][y - 1], 1))
    return graph

def convert_edge_to_grid_actions(edges):
    """
    Convert a list of edges to a string of actions in the grid base tile

    e.g. Edge(Node(Tile(1, 2), Tile(2, 2), 1)) => "S"
    """
    path = ''
    edge.from_node.data
    edge.to_node.data
    for edge in edges:
        if(edge.to_node.data.y - edge.from_node.data.y) < 0:
            path += 'N'
        elif(edge.to_node.data.y - edge.from_node.data.y) > 0:
            path += 'S'
        elif(edge.to_node.data.x - edge.from_node.data.x) > 0:
            path += 'E'
        elif(edge.to_node.data.x - edge.from_node.data.x) < 0:
            path += 'W'
        
    return path
