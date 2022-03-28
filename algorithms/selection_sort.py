def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list
