
# input: weights = [ 4, 6, 10, 15, 16 ], length = 5, limit = 21
# output: [ 3, 1 ]
# since these are the indices of weights 15 and 6 whose sum equals 21

def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    ans = None
    hash_table = {}
    index = 0

    for w in weights:
        if w in hash_table:
            if w + w == limit:
                ans = (index, hash_table[w])
        else:
            hash_table[w] = index
            index += 1

    if ans is None:
        for w in weights:
            diff = limit - w
            if diff in hash_table:
                ans = (hash_table[w], hash_table[diff])
    return ans
