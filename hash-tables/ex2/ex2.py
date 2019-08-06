#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    first_city = None
    last_city = None
    for i in range(length):
        t = tickets[i]

        if t.source is None:
            first_city = t.destination
            continue
        elif t.destination is None:
            last_city = t.source
            continue

        dest = hash_table_retrieve(hashtable, t.source)
        if dest is None:
            hash_table_insert(hashtable, t.source, t.destination)
        else:


    return route
