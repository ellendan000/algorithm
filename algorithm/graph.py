from collections import deque

def breadth_first_search(graph, source):
    search_queue = deque()
    search_queue += graph[source]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person.startswith('th'):
                return person
            else:
                search_queue += graph[person]
                searched.append(person)
    return None

def dijkstra_algorithm(graph, start, end):
    costs = {}
    parents = {}
    processed = []

    costs = {start: 0}
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors:
            new_cost = cost + neighbors[n]
            if n not in costs or costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    
    return (costs[end], concat_parent(parents, end))

def bellman_ford_algorithm(graph, start, end):
    costs = {}
    parents = {}
    edges = []

    for node in graph.keys():
        if node == start:
            costs[node] = 0
        else:
            costs[node] = float('inf')

    for i in range(0, len(graph.keys())):
        hasChange = False
        for node, neighbors in graph.items():
            for neighbor, cost in neighbors.items():
                if costs[node] + cost < costs[neighbor]:
                    costs[neighbor] = costs[node] + cost
                    parents[neighbor] = node
                    print(neighbor + ':' + node)
                    hasChange = True
        
        if hasChange == False:
            break

    for node, neighbors in graph.items():
            for neighbor, cost in neighbors.items():
                if costs[node] + cost < costs[neighbor]:
                    raise Exception('negative cyclic exists')

    return (costs[end], concat_parent(parents, end))


def concat_parent(parents, node):
    path = node
    current = parents[node]
    while current:
        path = f"{current}-{path}"
        current = parents.get(current)
    return path

def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node
        
