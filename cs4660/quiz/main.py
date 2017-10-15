"""
quiz2!
Use path finding algorithm to find your way through dark dungeon!
Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9
TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json
import codecs

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.
    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = urlopen(req, jsondataasbytes)
    reader = codecs.getreader('utf-8')
    return json.load(reader(response))

def bfs(init_id, dest_id):
    distance = {}
    parent = {}
    edge_to = {}
    queue = []
    queue.append((0, init_id));
    distance[init_id] = 0
    actions = []
    node_id = dest_id
    while len(queue) > 0:
        u = get_state(queue.pop()[1])
        neighbors = u['neighbors']
        for i in range(len(neighbors)):
            neigh = neighbors[i]
            if neigh['id'] not in distance:
                edge = transition_state(u['id'], neigh['id'])
                edge_to[neigh['id']] = edge
                distance[neigh['id']] = distance[u['id']] + 1
                parent[neigh['id']] = u['id']
                if neigh['id'] != dest_id:
                    queue.append((distance[neigh['id']], neigh['id']))
        queue = sorted(queue, key=lambda x:x[0])
        queue.reverse()
    while node_id in parent:
        actions.append(edge_to[node_id])
        node_id = parent[node_id]
    actions.reverse()

    return actions

def dijkstra(init_id, dest_id):

    distance = {}
    parent = {}
    edge_to = {}
    distance[init_id] = 0
    queue = []
    queue.append((0, init_id))
    visited = []
    actions = []
    node_id = dest_id
    while len(queue) > 0:
        u = get_state(queue.pop()[1])
        visited.append(u['id'])
        neighbors = u['neighbors']
        for i in range(len(neighbors)):
            v = neighbors[i]
            edge = transition_state(u['id'], v['id'])
            alt = distance[u['id']] + edge['event']['effect']
            if v['id'] not in visited and (v['id'] not in distance or alt > distance[v['id']]):
                if v['id'] in distance:
                    queue.remove((distance[v['id']], v['id']))
                queue.append((alt, v['id']))

                distance[v['id']] = alt
                parent[v['id']] = u['id']
                edge_to[v['id']] = edge
        queue = sorted(queue, key=lambda x:x[0]) 

    while node_id in parent:
        actions.append(edge_to[node_id])
        node_id = parent[node_id]

    actions.reverse()

    return actions

if __name__ == "__main__":
    
    bfs_result = bfs('7f3dc077574c013d98b2de8f735058b4', 'f1f131f647621a4be7c71292e79613f9')
    bfs_hp = 0

    dijkstra_result = dijkstra('7f3dc077574c013d98b2de8f735058b4', 'f1f131f647621a4be7c71292e79613f9')
    dij_hp = 0

    print("BFS")
    for action in bfs_result:
        bfs_hp += action['event']['effect']
        print(action)
    print("Total HP: "+ str(bfs_hp))

    print("Dijkstra")
    for line in dijkstra_result:
        dij_hp += line['event']['effect']
        print(action)
    print("Total HP: " + str(dij_hp))