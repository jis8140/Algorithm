from collections import defaultdict
from collections import deque


class graph:

    def __init__(self, adjacency_list: defaultdict(list)):
        self.adjacency_list = adjacency_list

    def bfs(self, v: int):
        discovered = [v]
        queue = deque([v])

        while queue:
            vertex = queue.popleft()

            for w in self.adjacency_list[vertex]:
                if w not in discovered:
                    discovered.append(w)
                    queue.append(w)

        return discovered


a = graph({
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3]
})
