"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates."""
import re
b_str = ""
solution = []
for call in calls:
    if '80' in call[0]:
        b_str += (str(call[1:2]))
s = b_str
ans = re.findall('\(([^)]+)', s)   
list_set = set(ans) 
unique_list = (list(list_set)) 
for x in unique_list:
    solution.append(x)

'''^^^ get all area codes inside parentheses ^^^'''
half = b_str.split(']')
better_half = str(half).split(' ') 

''' ^^^ get input to put through every_other to grab first half of numbers for area codes ^^^ '''

def every_other(listo):
    return listo[::2]

''' ^^^ grab first half of number that includes area code ^^^ '''
j = (every_other(better_half))

no_p = []
for blah in j:
    if "(" not in blah:
        no_p.append(blah)
final = []   
''' ^^^ grab numbers that aren't in parentheses ^^^'''
for meh in no_p:
    try:
        if int(meh[0]) > 6:
            final.append(meh.strip('"[\'').strip("'\","))
        if int(meh[0]) < 6:
            None
    except:
        final.append(meh.strip('"[\'').strip("'\","))
''' ^^^ grab numbers bigger than 6 or numbers enclosed in brackets ^^^'''
 
unique_list2 = []     
for x in final:
    unique_list2.append(x[0:4])
'''^^^ get first 4 characters ^^^'''
list_set2 = set(unique_list2)
unique_list2 = (list(list_set2))
for x in unique_list2:
    solution.append(x)
'''^^^ get unique four character combinations ^^^'''
sorted_solution = sorted(solution,key = int)
solution_a = ('\n'.join(map(str, sorted_solution)))
''' ^^^ sort the answer lexicographically ^^^ '''
print ("The numbers called by people in Bangalore have codes: \n{}".format(solution_a))

"""Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
