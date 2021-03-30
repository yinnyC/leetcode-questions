""" Problem 1136. Parallel Courses """


class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        in_count = {i: 0 for i in range(1, n + 1)}  # or in-degree
        for start_node, end_node in relations:
            graph[start_node].append(end_node)
            in_count[end_node] += 1
        queue = [node for node in graph if in_count[node] == 0]
        semester = 0
        studied_count = 0
        while queue:
            semester += 1
            next_queue = []
            for node in queue:
                studied_count += 1
                end_nodes = graph[node]
                for end_node in end_nodes:
                    in_count[end_node] -= 1
                    if in_count[end_node] == 0:
                        next_queue.append(end_node)
            queue = next_queue

        return semester if studied_count == n else -1
