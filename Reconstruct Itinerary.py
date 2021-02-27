"""332. Reconstruct Itinerary"""


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        [["A","B"],["B","C"]]
        output will be ["A","B","C"]
        -> BFS


        """
        node_to_visit = ["JFK"]  # A queue
        visited_node = []

        while len(node_to_visit) != 0 and len(tickets) != 0:
            cur_node = node_to_visit[0]
            # find matching indices
            indices = [i for i, ticket in enumerate(
                tickets) if ticket[0] == cur_node]
            if len(indices) == 1:
                destination = tickets[indices[0]][1]
                tickets.pop(indices[0])
            else:
                destinations = [tickets[i][1] for i in indices]
                destinations_dict = {tickets[i][1]: i for i in indices}
                destination = min(destinations)
                tickets.pop(destinations_dict[destination])
            node_to_visit.append(destination)
            visited_node.append(node_to_visit.pop(0))
        visited_node.append(node_to_visit.pop(0))
        return visited_node
