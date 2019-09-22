import csv

with open('StockList.txt', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
csv_reader
print(csv_reader.line_num)


