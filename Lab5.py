__author__ = 'hap', 'aps'

"""
Author: Herat Alkeshkumar Patel (hp9198@rit.edu) , Ashesh Piyush Sheth (as2462@rit.edu)
"""

import sys
import os


def search_prefix(prefix, dictionary, low, high):
    """
    Binary search to find the word of the lowest order in the list that starts with the prefix
    :param prefix: prefix
    :param dictionary: sorted list of words
    :param low: lower index for binary search
    :param high: higher index for binary search
    :return: matched word with the lowest order
    """
    if low > high:
        return "No match"
    mid = (low + high)//2
    item = dictionary[mid]
    if item.startswith(prefix):
        if dictionary[mid-1].startswith(prefix):
            return search_prefix(prefix, dictionary, low, mid-1)
        else:
            return item
    elif prefix < item:
        return search_prefix(prefix, dictionary, low, mid-1)
    else:
        return search_prefix(prefix, dictionary, mid+1, high)


def search_prefix_next(prefix, start, dictionary):
    """
    Linear search to find the remaining matches
    :param prefix: prefix
    :param start: index from where the linear search begins
    :param dictionary: sorted list of words
    :return: returns first match after 'start'
    """
    if (start != len(dictionary)) and (start != 0):
        newDictionary = dictionary[start:]
        for i in range(len(newDictionary)):
            if newDictionary[i].startswith(prefix):
                return newDictionary[i]
        return search_prefix_next(prefix, 0, dictionary)
    else:
        for i in range(len(dictionary)):
            if dictionary[i].startswith(prefix):
                return dictionary[i]


def lexicographic_sort(dictionary):
    """
    Sort the list in lexicographic order
    :param dictionary: unsorted list
    :return: sorted list
    """
    for start in range(len(dictionary)):
        for i in range(len(dictionary)-1, start, -1):
            if dictionary[i-1] > dictionary[i]:
                (dictionary[i-1], dictionary[i]) = (dictionary[i], dictionary[i-1])
    return dictionary
    

def main():
    """
    Gets file, sorts list of words and continually loops searching for prefix entered by user
    :return: None
    """
    filename = sys.argv[1]
    if not (os.path.isfile(filename)):
        print("File not found")
        exit()
    fd = open(filename)
    dictionary = list()
    for line in fd:
        dictionary.append(line.strip())
    dictionary = lexicographic_sort(dictionary)
    print("The sorted list:", end=" ")
    print(dictionary)
    print("Welcome to Auto-complete!\nUsage: Enter a prefix to auto-complete.\nEntering nothing will search for the next word with that prefix.\nEnter <QUIT> when asked for a prefix to exit.")
    prefix = input("Enter a prefix to search for: ")
    while prefix == "":
        print("Enter a prefix for the first time")
        prefix = input("Enter a prefix to search for: ")
    while True:
        while prefix == "":
            if result == "No match":
                result = search_prefix(prefixOld, dictionary, 0, len(dictionary)-1)
            else:
                result = search_prefix_next(prefixOld, dictionary.index(result)+1, dictionary)
            print(result)
            prefix = input("Enter a prefix to search for: ")
        if prefix == "<QUIT>":
            break
        result = search_prefix(prefix, dictionary, 0, len(dictionary)-1)
        print(result)
        prefixOld = prefix
        prefix = input("Enter a prefix to search for: ")
    print("Exiting Auto-complete! Good bye.")


if __name__ == "__main__":
    main()
