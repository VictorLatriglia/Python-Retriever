import csv

with open('hurricanes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\tIn {row[0]} there were {row[1]} hurricanes on average as in 2005: {row[2]},  2006: {row[3]},  2007: {row[4]},  2008: {row[5]},  2009: {row[6]},  2010: {row[7]},  2011: {row[8]},  2012: {row[9]},  2013: {row[10]},  2014: {row[11]},  2015: {row[12]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
