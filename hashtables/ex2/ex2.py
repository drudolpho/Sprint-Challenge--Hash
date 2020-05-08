#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    
    """
    YOUR CODE HERE
    """
    route = []
    hash_table = {}
    for t in tickets:
        hash_table[t.source] = t.destination

    key = "NONE"
    for i in range(1, length):
        route.append(hash_table[key])
        key = hash_table[key]
    route.append("NONE")
    return route
