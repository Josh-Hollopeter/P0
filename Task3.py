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
part2 = []
for call in calls:
    if '080' in call[0]:
        b_str += (str(call[1:2]))
s = b_str
ans = re.findall('\(([^)]+)', s)   
list_set = set(ans) 
unique_list = (list(list_set)) 
for x in unique_list:
    solution.append(x)
''' ^^^ get numbers inside area parentheses ^^^ '''
half = b_str.split(']')
better_half = []

for h in half:
    better_half.append(h[0:8])

''' ^^^ get first half where area code resides ^^^ '''

no_p = []
for blah in half:
    if "(" not in blah:
        no_p.append(blah)
final = []   
''' ^^^ grab numbers that aren't in parentheses ^^^'''
for meh in no_p:
    try:
        if int(meh[0]) > 6:
            final.append(meh.strip("['").strip("',"))
        if int(meh[0]) < 6:
            None
    except:
        final.append(meh.strip("['").strip("',"))
''' ^^^ grab numbers bigger than 6 or numbers enclosed in brackets ^^^'''
 
unique_list2 = []     
for x in final:
    try:
        if int(x[0]):
            unique_list2.append(x[0:4])
    except:
        None
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
f_str = ""

count = 0
count2 = 0
f_str = ""
for call in calls:
    if '080' in call[0]:
        f_str += (str(call[1:2]))

part2 = f_str.split(']')
''' ^^^ grab all calls from bangalore and brackets to make splitting easy ^^^'''
for x in half:
    if '080' in x[0:6]:
        count +=1
    else:
        count2 +=1
''' count them calls '''
part2_a = (count/(count+count2))
b_answer = round(part2_a,2)
print ("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(b_answer))
