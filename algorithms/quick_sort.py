def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    left = [x for x in list[1:] if x <= pivot]
    right = [x for x in list[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
