def sort(arr, callback):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []
    for i in range(1, len(arr)):
        item = arr[i]
        if callback(item, pivot):
            left.append(item)
        else:
            right.append(item)

    return sort(left, callback) + [pivot] + sort(right, callback)


def is_anagram(first_string, second_string):
    first_list = sort(first_string, lambda a, b: a.lower() < b.lower())
    second_list = sort(second_string, lambda a, b: a.lower() < b.lower())

    first = "".join(first_list).lower()
    second = "".join(second_list).lower()

    return (first, second, first == second and first != "")
