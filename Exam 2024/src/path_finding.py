import heapq
from typing import Callable, TypeVar, List, Tuple, Dict

Node = TypeVar('Node')


def build_path(
    predecessors: Dict[Node, Node | None],
    goal: Node
) -> List[Node]:
    path = []
    while True:
        path.append(goal)
        prev = predecessors.get(goal)
        if prev is None:
            break
        goal = prev
    return path[::-1]


def dijkstra(
    get_neighbors: Callable[[Node], List[Tuple[Node, float]]],
    start_state: Node,
    goal_state: Node,
) -> List[Node] | None:
    distances = {start_state: 0.}
    predecessors: Dict[Node, Node | None] = {start_state: None}

    # Priority queue to store vertices that are being minimized
    pq: List[Tuple[float, Node]] = [(0, start_state)]

    while pq:
        # Get the node with the lowest distance
        current_distance, current_node = heapq.heappop(pq)

        # Check neighbors of current node
        for neighbor, weight in get_neighbors(current_node):
            distance = current_distance + weight

            # If we've found a shorter path, update it
            if distance < distances.get(neighbor, float('infinity')):
                distances[neighbor] = distance
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (distance, neighbor))

        if current_node == goal_state:
            return build_path(predecessors, current_node)

    return None


def a_star(
    get_neighbors: Callable[[Node], List[Tuple[Node, float]]],
    start_state: Node,
    goal_state: Node,
    heuristic: Callable[[Node, Node], float]
) -> List[Node] | None:
    # Initialize distances and predecessors
    g_scores = {start_state: 0.}
    f_scores = {start_state: heuristic(start_state, goal_state)}
    predecessors: Dict[Node, Node | None] = {start_state: None}

    # Priority queue to store vertices that are being minimized
    pq: List[Tuple[float, Node]] = [(0, start_state)]

    while pq:
        # Get the node with the lowest distance
        current_distance, current_node = heapq.heappop(pq)

        # Check neighbors of current node
        for neighbor, weight in get_neighbors(current_node):
            g_score = current_distance + weight

            # If we've found a shorter path, update it
            if g_score < g_scores.get(neighbor, float('infinity')):
                g_scores[neighbor] = g_score
                f_scores[neighbor] = g_score + heuristic(neighbor, goal_state)
                predecessors[neighbor] = current_node
                heapq.heappush(pq, (g_score + heuristic(neighbor, goal_state), neighbor))

        if current_node == goal_state:
            return build_path(predecessors, current_node)

    return None
