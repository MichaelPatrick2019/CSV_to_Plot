#Quick script that demonstrates functionality of
#CSVtoPlot vs a direct read from a file

import csv
import matplotlib.pyplot as plt
import numpy

if __name__ == '__main__':
    with (open('ExampleCSV.csv', encoding="utf-8", newline='')) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=' ')

        x_array = []
        y_array = []

        is_first = True;
        # y_value key to list of all x_values
        for row in csvreader:
            split_string = row[0].split(',')

            if (is_first):  # skip name
                is_first = False
                continue

            x_array.append(float(split_string[1]))
            y_array.append(float(split_string[2]))

        #fig, ax = plt.subplots()
        #ax.plot(x_array, y_array)
        #plt.show()

        #plot
        plt.scatter(x_array, y_array)

        #trend line
        z = numpy.polyfit(x_array, y_array, 1) #Returns vector of coefficients
        p = numpy.poly1d(z) #Generates a polynomial from coefficients
        plt.plot(x_array, p(x_array), 'r-')

        #Output
        plt.show()