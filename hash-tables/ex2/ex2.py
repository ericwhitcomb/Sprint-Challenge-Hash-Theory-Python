#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for i in range(length):
        t = tickets[i]
        if t.source == "NONE":
            route[0] = t.destination
        else:
            hash_table_insert(hashtable, t.source, t.destination)
        
    for i in range(1, length):
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route
