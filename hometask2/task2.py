"""Task 2: The most popular word"""

def get_list_of_words():
    """return list of input words"""
    list_of_words = []
    while True:
        new_string = input()
        if not new_string:
            break
        list_of_words.extend(new_string.split())
    return(list_of_words)

#transform text to list of words
text = get_list_of_words()

#create the dictionary
dictionary = {}
for word in text:
    count = dictionary.get(word, 0)
    dictionary[word] = count + 1

#find the most popular word
max_count = 0
is_popular = 1
for word in dictionary:
    if max_count < dictionary[word]:
        max_count = dictionary[word]
        popular_word = word
        is_popular = 1
    elif max_count == dictionary[word]:
        is_popular = 0

#print the answer
if is_popular:
    print(popular_word)
else:
    print("-")
