from collections import defaultdict


class graph:

    def __init__(self, adjacency_list: defaultdict(list)):
        self.adjacency_list = adjacency_list

    def recursive_dfs(self, v: int, discovered=[]):
        discovered.append(v)

        for w in self.adjacency_list[v]:
            if w not in discovered:
                discovered = self.recursive_dfs(w, discovered)

        return discovered

    def iterative_dfs(self, v: int):
        discovered = []
        stack = [v]

        while stack:
            vertex = stack.pop()

            for w in self.adjacency_list[vertex]:
                if w not in discovered:
                    stack.append(w)

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
