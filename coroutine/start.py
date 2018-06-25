def eager_range(up_to):
    """Create a list of integers, from 0 to up_to, exclusive."""
    sequence = []
    index = 0
    while index < up_to:
        sequence.append(index)
        index += 1
    return sequence


def lazy_range(up_to):
    """Generator to return the sequence of integers from 0 to up_to, exclusive."""
    index = 0
    while index < up_to:
        yield index
        index += 1


if __name__ == '__main__':
    print(eager_range(10))
    arr = list(lazy_range(10))
    print(arr)
