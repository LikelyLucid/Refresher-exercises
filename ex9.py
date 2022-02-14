"""Write a function longest_word(string_list) that is given a list of words and prints the longest word in the list. If there are two words of the same length, print the first one:"""
def longest_word(string_list):
    longest = string_list[0]
    for word in string_list:
        if len(word) > len(longest):
            longest = word
    return longest

words = ["jack", "tomato", "cat"]
print(longest_word(words))
