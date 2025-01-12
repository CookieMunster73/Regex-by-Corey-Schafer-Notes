import re

# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)

# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String

# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group

# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)


# #### Sample Regexs ####

# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+

###################################################################################

# .findall(variable_name) = print all matches, splits into tuple if groups are present
# .finditer(variable_name) = print matches plus span and object info
# .sub(r'\value\value', variable_name) = replace returned pattern with specific groups in pattern
# .match(variable_name) = return match at start, else None
# .search(variable_name) = return match, else None

###################################################################################

# (r"", re.IGNORECASE or re.I) = removes case sensitivity 


text_to_search = r'''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'

# print('\tTab')
# print(r'\tTab') # r strings print raw text data, regardless of escapes except for some specific characters

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z].*')

matches = pattern.finditer(text_to_search)

# match_count = 0
# for match in matches:
#     match_count += 1
#     print(match)
# if match_count == 0:
#     print("No Matches Found")

# with open('data.txt', 'r') as f:
#     contents = f.read()

#     matches = pattern.finditer(contents)

#     match_count = 0
#     for match in matches:
#         match_count += 1
#         print(match)
#     if match_count == 0:
#         print("No Matches Found")

# print(text_to_search[155:167])

#########################################################################################################


import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-z]{3}')
# pattern = re.compile(r'[\w.-]+@\w.-]+\.[a-z]{3}')

matches = pattern.finditer(emails)

for match in matches:
    print(match)

#########################################################################################################

import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?([a-zA-Z0-9.-]+)(\.(com|gov))')

# subbed_url = pattern.sub(r'\2\3', urls)

# print(subbed_url)

# matches = pattern.finditer(urls)

# for match in matches:
#     print(match)
#     print(f"{match.group(2)}{match.group(3)}")

# matches = pattern.findall(urls)

# for match in matches:
#     print(match)

##########################################################################################################


sentence = 'Start a sentence and then bring it to an end'

pattern = re.compile(r'sEnTenCe', re.I)

matches = pattern.search(sentence)

# print(matches)

# match_count = 0
# for match in matches:
#     match_count += 1
#     print(match)
# if match_count == 0:
#     print("No Matches Found")

