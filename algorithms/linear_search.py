def linear_search(list):
    for i in range(len(list)):
        if list[i] == "":
            return i
    return len(list)
