import algorithm.graph as ga

graph_1 = {
    'you': ['alice', 'bob', 'claire'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': []
}

graph_2 = {
    'start': {
        'A': 6,
        'B': 2
    },
    'A': {
        'fin': 2
    },
    'B': {
        'A': 3,
        'fin': 7
    },
    'fin': {}
}

graph_3 = {
    'start':{
        'A': 5,
        'B': 3
    },
    'A': {
        'C': 2,
        'D': 2
    },
    'B': {
        'C': 1,
        'E': 6
    },
    'C': {
        'end': 5
    },
    'D': {
        'C': 3,
        'end': 4
    },
    'E': {
        'end': 1
    },
    'end': {}

}

def test_breadth_first_search():
    assert 'thom' == ga.breadth_first_search(graph_1, 'you')

def test_dijkstra_algorithm():
    assert (7, 'start-B-A-fin') == ga.dijkstra_algorithm(graph_2, 'start', 'fin')

def test_bellman_ford_algorithm():
    assert (9, 'start-B-C-end') == ga.bellman_ford_algorithm(graph_3, 'start', 'end')

def test_find_lowest_cost_node():
    assert 'B' == ga.find_lowest_cost_node(graph_2['start'], [])