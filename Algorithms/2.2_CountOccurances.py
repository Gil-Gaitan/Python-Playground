# Count Occurrences: Given a list, count how many times each element appears using loops.


def count_occurrences(list):
    count_dict = {}
    for item in list:
        count_dict[item] = count_dict.get(item, 0) + 1
    return count_dict


# tests

print(count_occurrences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(count_occurrences([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))

# Output:
# {1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1}
# {1: 10}
