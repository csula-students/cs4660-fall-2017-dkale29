"""
Searches module defines all different search algorithms
"""
import math

def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    distance= {}
    parent = {}
    edge = {}
    action = []
    end_node = dest_node
    queue = []
    queue.append((0, initial_node));
    distance[initial_node] = 0

    while len(queue) > 0:
        i = queue.pop()[1]

        for node in graph.neighbors(i):
            if node not in distance:
                edge[node] = graph.distance(i, node)
                distance[node] = distance[i] + edge[node].weight
                parent[node] = i
                if node != dest_node:
                    queue.append((distance[node], node))
        queue = sorted(queue, key=lambda x:x[0])
        queue.reverse()
    while end_node in parent:
        action.append(edge[end_node])
        end_node = parent[end_node]

    action.reverse()

    return action

def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    for node in graph.neighbors(initial_node):
        if node == dest_node:
            return [graph.distance(initial_node, dest_node)]
        else:
            path = dfs(graph, node, dest_node)
            if path != []:
                action = [graph.distance(initial_node, node)]
                action.extend(path)
                return action
    return []

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    distance = {}
    previous = {}
    action = {}
    distance[initial_node] = 0
    actions = []
    current_node = dest_node
    queue = []
    queue.append((0, initial_node))

    while len(queue) > 0:
        i = queue.pop()[1]
        for v in graph.neighbors(i):
            edge = graph.distance(i, v)
            dist = distance[i] + edge.weight
            if v not in distance or dist < distance[v]:
                if v in distance:
                    queue.remove((distance[v], v))
                queue.append((dist, v))
                distance[v] = dist
                previous[v] = i
                action[v] = edge
        queue = sorted(queue, key=lambda x:x[0])
        queue.reverse()

    while current_node in previous:
        actions.append(action[current_node])
        current_node = previous[current_node]

    actions.reverse()

    return actions

def heuristic(node, goal):
    dx = abs(node.data.x - goal.data.x)
    dy = abs(node.data.y - goal.data.y)
    return math.sqrt(dx * dx + dy * dy)

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    parent = {}
    edge = {}
    visit = []
    not_visit = [(0, initial_node)]

    g_score = {}
    g_score[initial_node] = 0
    f_score = {}
    f_score[initial_node] = heuristic(initial_node, dest_node)

    while len(not_visit) > 0:
        i = not_visit.pop()[1]
        if i == dest_node:
            current_node = i
            actions = []
            while current_node in parent:
                actions.append(edge[current_node])
                current_node = parent[current_node]
            actions.reverse()
            return actions
        visit.append(i)

        for node in graph.neighbors(i):
            if node not in visit:
                edge = graph.distance(i, node)
                g_scoretemp = g_score[i] + edge.weight
                if g_scoretemp < g_score[node]:
                    not_visit.remove((f_score[node], node))
                    parent[node] = i
                    edge[node] = edge
                    g_score[node] = g_scoretemp
                    f_scoretemp = g_scoretemp + heuristic(node, dest_node)
                    f_score[node] = f_scoretemp
                    not_visit.append((f_score[node], node))
                if node not in g_score:
                    not_visit.append((float('val'), node))
                    g_score[node] = float('val')
                    f_score[node] = float('val')                
        not_visit = sorted(not_visit, key=lambda x:x[0])
        not_visit.reverse()
    return []