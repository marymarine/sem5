"""Task 3: Phone number"""
import itertools

#create dictionary
dictionary = {
    #'1': (''),
    '2': ('a', 'b', 'c'),
    '3': ('d', 'e', 'f'),
    '4': ('g', 'h', 'i'),
    '5': ('j', 'k', 'l'),
    '6': ('m', 'n', 'o'),
    '7': ('p', 'q', 'r', 's'),
    '8': ('t', 'u', 'v'),
    '9': ('w', 'x', 'y', 'z'),
    '0': ('_')
}

#get all combinations
number = input()
list_of_digits = list(number)
alphabet = []
for digit in list_of_digits:
    alphabet.append(dictionary[digit])
all_combinations = list(itertools.product(*alphabet))

#get list of sequences
output = []
for sequence in all_combinations:
    output.append("".join(sequence))

#print the answer
print(output)
