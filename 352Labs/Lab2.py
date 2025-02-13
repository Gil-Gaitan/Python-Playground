import random

# Name:     Gil Gaitan
# Course:   ICS 352-50 Machine Learning - Brad Armitage - Spring 2025
# Lab  2 - Python Exercises

# Lab 2
# Overview of List, Tuple, Dictionary, and Set
# Assignment Programs:
#   1. Summarizing Letters in a String
#   2. Counting Duplicate words
#   3. Numbers Frequency
#   4. Is a Sentence Sorted


# Program 1: Summarizing Letters in a String
def summarize_letters(string):
    letter_frequency_dictionary = {}
    for letter in string:
        if letter.isalpha():  # Only count letters
            letter = letter.lower()  # Turn letter to lowercase
            if letter in letter_frequency_dictionary:  # Add to dictionary
                letter_frequency_dictionary[letter] += 1
            else:
                letter_frequency_dictionary[letter] = 1
    return letter_frequency_dictionary


def summarize_letters_test():
    string = "The quick brown fox jumps over the lazy dog"
    letter_frequency_dictionary = summarize_letters(string)
    print("Letter\tFrequency")
    for letter, frequency in letter_frequency_dictionary.items():
        print(f"{letter}\t{frequency}")
    print(
        "All letters of the alphabet are present"
        if set(letter_frequency_dictionary.keys()) == set("abcdefghijklmnopqrstuvwxyz")
        else "Not all letters of the alphabet are present"
    )


print("\nSummarizing Letters in a String:")
summarize_letters_test()


# Program 2: Counting Duplicate words


def count_duplicate_words(sentence):
    words = sentence.split()
    word_frequency_dictionary = {}
    for word in words:
        word = word.lower()
        if word in word_frequency_dictionary:
            word_frequency_dictionary[word] += 1
        else:
            word_frequency_dictionary[word] = 1
    return word_frequency_dictionary


def count_duplicate_words_test():
    sentence = "The quick brown fox jumps over the lazy dog and the quick brown fox"
    word_frequency_dictionary = count_duplicate_words(sentence)
    print("Word\tFrequency")
    for word, frequency in word_frequency_dictionary.items():
        if frequency > 1:
            print(f"{word}\t{frequency}")


print("\nCounting Duplicate Words:")
count_duplicate_words_test()

# Program 3: Numbers Frequency


def generate_random_numbers():
    random_numbers = [random.randint(1, 10) for _ in range(100)]
    return random_numbers


def numbers_frequency():
    random_numbers = generate_random_numbers()
    frequency_dictionary = {}
    for number in random_numbers:
        if number in frequency_dictionary:  # Add to dictionary
            frequency_dictionary[number] += 1
        else:
            frequency_dictionary[number] = 1
    return frequency_dictionary  # Return the dictionary


def numbers_frequency_test():
    frequency_dictionary = numbers_frequency()  # make a dictionary
    print("Number\tFrequency")
    for number, frequency in frequency_dictionary.items():
        print(f"{number}\t{frequency}")


print("\nNumbers Frequency:")
numbers_frequency_test()

# Program 4: Is a Sentence Sorted
# 1.	Search for the meaning of sequences in Python, and explain what is a sequence in python?
# 2.	Create a function is_ordered that receives a sequence and returns true if the elements are in sorted order. Test your function with sorted and unsorted lists, tuples and strings.


def is_ordered(sequence):
    return list(sequence) == sorted(sequence)


def is_ordered_test():
    print(is_ordered([1, 2, 3, 4, 5]))
    print(is_ordered([5, 4, 3, 2, 1]))
    print(is_ordered((1, 2, 3, 4, 5)))
    print(is_ordered((5, 4, 3, 2, 1)))
    print(is_ordered("abcde"))
    print(is_ordered("edcba"))


print("\nIs a Sentence Sorted:")
is_ordered_test()
