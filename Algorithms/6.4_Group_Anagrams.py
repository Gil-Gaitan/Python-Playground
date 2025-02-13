# Group a list of strings into anagrams.

# Approach:
# We can group anagrams by sorting each string and using the sorted
# string as a key in a dictionary. The value corresponding to each key
# will be a list of anagrams. We iterate through the list of strings,
# sort each string, and add it to the corresponding list in the dictionary.
# Finally, we return the values of the dictionary as a list of grouped anagrams.


def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        sorted_s = "".join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]

    return list(anagrams.values())


# Test cases
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))
