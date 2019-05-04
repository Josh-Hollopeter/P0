"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
'''import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list()

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list()'''


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

import pandas
colnames = ['sending_number', 'receiving_number', 'date', 'calltime']
data = pandas.read_csv('calls.csv', names=colnames)
'''read calls.csv ^^^'''
colnames = ['sending_number_t', 'receiving_number_t', 'date_t']
data_t = pandas.read_csv('texts.csv', names=colnames)
'''read texts.csv ^^^'''
columns = [data.sending_number,data.receiving_number,data_t.sending_number_t,data_t.receiving_number_t]
all_call_columns = pandas.concat(columns)
'''concatenate all columns ^^^'''
total_num_calls = (all_call_columns.nunique())
'''find unique values for all phone number columns combined ^^^'''
print ("There are {} different telephone numbers in the records".format(total_num_calls))



