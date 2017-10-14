"""
quiz2!

Use path finding algorithm to find your way through dark dungeon!

Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9

TODO: implement BFS
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json

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
    response = json.load(urlopen(req, jsondataasbytes))
    return response

if __name__ == "__main__":
    # Your code starts here
    '''
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    print(empty_room)
    print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))


    dark_room = get_state('f1f131f647621a4be7c71292e79613f9')
    print(dark_room)
    print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))
    '''
    result = bfs('7f3dc077574c013d98b2de8f735058b4','f1f131f647621a4be7c71292e79613f9')
def bfs(initial, dest)
    
    queue = []

    distance = [initial] = 0

    while (!queue.isEmpty()):
        u = queue.dequeue()

        for i in range(len(neighbors))
            neigh = neighbors[i]
            if()

    return result
'''
function BFS(v) {
    for (node in G) {
        node.distance = Number.MAX_VALUE;
        node.parent = null;
    }

    // create empty queue Q
    var queue = new Queue();
    // Best first search - use priority queue (lowest number goes first)
    var result = [];
    var endTile = null;

    v.distance = 0;
    queue.enqueue(v);

    while (!queue.isEmpty()) {
        var u = queue.dequeue();

        for (node in Graph.neighbors(u)) {
            if (node.distance == Number.MAX_VALUE) {
                node.distance = u.distance + edge.value
                // note that I'm leaving edge value up to
                // you to implement
                node.parent = u;
                if (Graph.isGoal(node)) {
                  endTile = u;
                }
                queue.enqueue(node);
            }
        }
    }
    // back trace from goal to start
    while (endTile.parent != null) {
      result.add(Edge(endTile.parent, endTile));
      endTile = endTile.parent;
    }
    // remember to reverse the result before return
    return result.reverse();
}'''