#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    if length < 2:
        return None

    for i in range(length):
        # calculate other value
        other_value = limit - weights[i]

        # retrieve index of other value
        j = hash_table_retrieve(ht, other_value)

        # check if j not null and j more than i
        if j is not None and j > i:
            return (j, i)
        elif j is not None: # or check if j not null which means j is less than i
            return (i, j)
        else: # else insert in ht
            hash_table_insert(ht, weights[i], i)


    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
