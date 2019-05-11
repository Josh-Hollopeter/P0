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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
sending, receiving = set(), set()
for row in calls:
    sending.add(row[0])
    receiving.add(row[1])

for row in texts:
    receiving.add(row[0])
    receiving.add(row[1])

list1 = list(set(sending) - set(receiving))
sorted_solution = sorted(list1,key = str)

solution = ('\n'.join(map(str, sorted_solution)))

print ("These numbers could be telemarketers:\n{}".format(solution))
