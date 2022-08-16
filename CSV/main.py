import csv
from Graphics import CreateGraph


class Plot:
    pass


with open('hurricanes.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    xAxisLabel = 'Años'
    yAxisLabel = 'Cantidad de huracanes'
    xAxis = ['2005', '2006', '2007', '2008', '2009',
             '2010', '2011', '2012', '2013', '2014', '2015']
    plots = []
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            plot = Plot()
            plot.x = xAxis
            plot.y = [int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(
                row[7]), int(row[8]), int(row[9]), int(row[10]), int(row[11]), int(row[12])]
            plot.label = row[0]
            plots.append(plot)
            line_count += 1
    CreateGraph(plots, xAxisLabel, yAxisLabel)
    print(f'Processed {line_count} lines.')
