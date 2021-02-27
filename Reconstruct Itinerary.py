"""332. Reconstruct Itinerary"""


def findItinerary(tickets):
    node_to_visit = ["JFK"]
    visited_node = []

    while len(node_to_visit) != 0 and len(tickets) != 0:
        cur_node = node_to_visit[0]
        # Find the ticke
        target_tickets = [
            ticket for ticket in tickets if ticket[0] == cur_node]
        # Pick Destination
        if len(target_tickets) == 1:  # case 1 only one match
            destination = target_tickets[0][1]
        else:  # case 2 1.Check if the destination has a connect flight
            destinations = [ticket[1] for ticket in target_tickets]
            for destination in destinations:
                temp_tickets = tickets.copy()
                temp_tickets.pop(tickets.index([cur_node, destination]))
                temp_froms = [ticket[0] for ticket in temp_tickets]
                if destination not in temp_froms:
                    destinations.remove(destination)
            # case 2 2.Compare the destination
            if len(destinations) == 1:
                destination = destinations[0]
            else:
                destination = min(destinations)

        tickets.pop(tickets.index([cur_node, destination]))
        node_to_visit.append(destination)
        visited_node.append(node_to_visit.pop(0))
    visited_node.append(node_to_visit.pop(0))
    return visited_node


tickets = [["JFK", "SFO"], ["JFK", "ATL"], [
    "SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
print(findItinerary(tickets))
