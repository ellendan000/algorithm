import algorithm.search as se

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

def test_breadth_first_search():
    assert 'thom' == se.breadth_first_search(graph_1, 'you')

def test_dijkstra_algorithm():
    assert (7, 'start-B-A-fin') == se.dijkstra_algorithm(graph_2, 'start', 'fin')

def test_find_lowest_cost_node():
    assert 'B' == se.find_lowest_cost_node(graph_2['start'], [])