"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
import pandas
colnames = ['sending_number', 'receiving_number', 'date', 'calltime']
data = pandas.read_csv('calls.csv', names=colnames)
''' ^^^ read_csv and name columns ^^^ '''
all_call_columns = data.groupby(['sending_number']).sum()
all_call_columns2 = data.groupby(['receiving_number']).sum()
''' ^^^ group by phone numbers and sum() times ^^^ '''
group = all_call_columns + all_call_columns2
''' ^^^ add groups together ^^^ '''
answer = (group.sort_values(by=['calltime'],ascending = False))
''' ^^^ sort to get longest call time ^^^ '''
format2 =  (answer.to_string(index=False)[9:22])
format1 = (answer.index[0])
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(format1,format2))