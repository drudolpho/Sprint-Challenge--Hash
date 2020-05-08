def has_negatives(a):

    """
    YOUR CODE HERE
    """
    result = []
    hash_table = {}

    for i in a:
        opp = i * -1
        if opp in hash_table:
            result.append(abs(opp))
        else:
            hash_table[i] = i

    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
