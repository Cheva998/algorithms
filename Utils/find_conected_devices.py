from collections import deque

def build_adjacency(connections: list) -> dict:
    adj = {}
    for sender, receiver in connections:
        if sender not in adj:
            adj[sender] = set()
        adj[sender].add(receiver)
    return adj

def find_reachables(connections: list, source: str) -> set:
    adjacency = build_adjacency(connections)

    reachables = set()
    if source not in adjacency:
        return reachables

    discovered = {source}
    frontier = [source]

    while len(frontier) > 0:
        current = frontier.pop()
        for device in adjacency.get(current, []):
            if device not in discovered:
                frontier.append(device)
                discovered.add(device)
                reachables.add(device)

    return reachables

def find_minimum_hops(connections: list, source: str, target: str) -> int:
    adjacency = build_adjacency(connections)
    
    discovered = {source}

    frontier = deque()
    counter = 0
    frontier.append((source, counter))

    while len(frontier) > 0:
        current, counter = frontier.popleft()
        counter += 1
        for device in adjacency.get(current, {}):
            if device == target:
                return counter
            if device not in discovered:
                discovered.add(device)
                frontier.append((device, counter))
    return None

def test_reachables(func_to_test):
    connections1 = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "E"),
        ("E", "F"),
        ("D", "F"),
        ("F", "G")
    ]
    connections2 = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "E"),
        ("E", "F"),
        ("D", "F"),
        ("F", "G"),
        ("G", "A")
    ]
    connections3 = [
        ("B", "D"),
        ("C", "E"),
        ("E", "F"),
        ("D", "F"),
        ("F", "G"),
        ("G", "A"),
        ("A", "B"),
        ("A", "C"),
    ]
    connections4 = [
        ("B", "D"),
        ("C", "E"),
        ("E", "F"),
        ("D", "F"),
        ("F", "G"),
        ("G", "A")
    ]

    expected1 = {"B", "C", "D", "E", "F", "G"}
    expected2 = {"B", "C", "D", "E", "F", "G"}
    expected3 = {"B", "C", "D", "E", "F", "G"}
    expected4 = set()
    assert func_to_test(connections1, "A") == expected1
    assert func_to_test(connections2, "A") == expected2
    assert func_to_test(connections3, "A") == expected3
    assert func_to_test(connections4, "A") == expected4
    print("all passed")

def test_hops(func_to_test):
    connections1 = [("A", "B"),("A", "C"),("B", "D"),("C", "E"),("E", "F"),("D", "F"),("F", "G")]
    expected_hops1 = 1
    expected_hops2 = 2
    expected_hops3 = 3
    expected_hops4 = None

    assert(func_to_test(connections1, "A", "C") == expected_hops1)
    assert(func_to_test(connections1, "A", "D") == expected_hops2)
    assert(func_to_test(connections1, "A", "F") == expected_hops3)
    assert(func_to_test(connections1, "A", "A") == expected_hops4)
    print("all passed")

test_reachables(find_reachables)
test_hops(find_minimum_hops)
