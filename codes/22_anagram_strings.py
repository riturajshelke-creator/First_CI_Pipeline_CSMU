def is_anagram(first, second):
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()

    if len(first) != len(second):
        return False

    return sorted(first) == sorted(second)