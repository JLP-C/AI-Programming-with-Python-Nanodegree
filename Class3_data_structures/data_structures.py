#ejercicios clase 3: Data Structures

# 1.- List indexing
month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
print(days_in_month[month-1])

# 2.- Slicing lists
eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']


# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates[-3:])

# 3.- Dictionaries
# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {}
population["Shanghai"] = 17.8
population.update({"Istambul":13.3})
population.update(dict(Karachi=13.0))          #Karachi sin comillas!!!!
population.update(Mumbai=12.5)                 #Mumbai sin comillas!!!!
print(population)

# 4. working with dictionaries
elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn'
elements['hydrogen']['is_noble_gas'] = 'N'
elements['helium'].update(is_noble_gas='Y')
print(elements)

# 5. split, join, len
verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"

# split verse into list of words
list_of_words = verse.split()
print(" - ".join(list_of_words))
#print(list_of_words)

# convert list to a data structure that stores unique elements
unique_elements = set(list_of_words)
print(" - ".join(unique_elements))

# print the number of unique words
print(len(list_of_words))
print(len(unique_elements))

# 6. build a dictionary that contains the words in verse as keys and the number of apperances as Value
word_occur = {}
for word in unique_elements:
    occurrences = list_of_words.count(word)
    word_occur[word] = occurrences
print(word_occur)

# 7. questions on Dictionary
# How many unique words are in verse_dict?
counter = 0
for key in word_occur:
    if word_occur[key] == 1:
        counter += 1
print(counter)

# find whether 'breathe' is a key in the dictionary
print('breathe' in word_occur)

# create and sort a list of the dictionary's keys
key_list = sorted(word_occur.keys())
print(key_list)

# get the first element in the sorted list of keys
print(key_list[0])
