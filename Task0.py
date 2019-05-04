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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
import pandas
colnames = ['sending_number', 'receiving_number', 'date', 'calltime']
data = pandas.read_csv('calls.csv', names=colnames)
tail = data.tail(1).index.item()

colnames = ['sending_number_t', 'receiving_number_t', 'date_t']
data_t = pandas.read_csv('texts.csv', names=colnames)
head = data_t.head(1).index.item()
print("First record of texts, {} texts {} at time {}".format(data_t['sending_number_t'][head],data_t['receiving_number_t'][head],
      data_t['date_t'][head],data['calltime'][head]))


print("Last record of calls, {} calls {} at time {} lasting {} seconds".format(data['sending_number'][tail],data['receiving_number'][tail],
      data['date'][tail],data['calltime'][tail]))
