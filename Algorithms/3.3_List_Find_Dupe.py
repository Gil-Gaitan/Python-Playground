# find duplicate in an array and return index

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 10]


def find_duplicate(lst):  # returns indexes of duplicates
    seen = {}
    for i, item in enumerate(lst):  # enumerate returns index and value
        if item in seen:
            return seen[item], i
        seen[item] = i
    return None


def find_dupes_with_nums(lst):  # returns indexes and the duplicated value
    seen = {}
    for i, item in enumerate(lst):
        if item in seen:
            return seen[item], i, item
        seen[item] = i
    return None


def Find_dupes_alt(lst):  # return index of dulplicates without enumerate
    seen = {}
    for i in range(len(lst)):
        if lst[i] in seen:
            return seen[lst[i]], i
        seen[lst[i]] = i
    return None


print(find_duplicate(list1))  # (1, 9)
print(find_dupes_with_nums(list1))  # (1, 9, 2)
print(Find_dupes_alt(list1))  # (1, 9)
