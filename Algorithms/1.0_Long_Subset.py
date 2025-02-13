list = [3, 2, 2, 1, 1, 1, 1, 4, 5, 6, 3, 3, 2]


def get_longest_sublist(lst):
    longest_sublist = []
    current_sublist = []
    for i in range(len(lst) - 1):
        if lst[i] == lst[i + 1]:
            current_sublist.append(lst[i])
        else:
            current_sublist.append(lst[i])
            if len(current_sublist) > len(longest_sublist):
                longest_sublist = current_sublist
            current_sublist = []
    return longest_sublist


print(get_longest_sublist(list))
