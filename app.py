import io
import re

filename = 'altavista_2002_data'

file_data = io.open(filename, encoding='latin-1')

dictionary = {}

lines = file_data.readlines()

for line in lines:
    line_list = re.split(r'\t+', line.rstrip('\t'))

    identity = line_list[0]

    if identity in dictionary:
        dictionary[identity] += 1
    else:
        dictionary[identity] = 1

total_search_count = 0
number_of_identities = len(dictionary)

for identity, search_count in dictionary.items():
    total_search_count += search_count

searches_per_identity = total_search_count / number_of_identities

print('total search count:', total_search_count)
print('number of identities:', number_of_identities)
print('There were {} searches per identity.'.format(searches_per_identity))

