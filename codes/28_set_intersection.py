def set_intersection(first, second):
    result = set()

    for element in first:
        if element in second:
            result.add(element)

    return result