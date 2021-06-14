#Michael Patrick
#6/13/21
#Matplot from CSV example
#Takes a CSV value, formatted as specified below,
#and generates a plot using MatPlotLib.

import csv
import matplotlib.pyplot as plt
import numpy

if __name__ == '__main__':
    with (open('ExampleCSV.csv', newline='')) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ' ', quotechar='|')

        x_axis = []
        y_axis = []



        #print data from csv file, add data to arrays
        firstRow = False
        for row in csvreader:
            split_line = row[0].split(',')
            #Expects three columns: name, length, height
            print(f'{split_line[0]:15} {split_line[1]:15} {split_line[2]:15}')

            if(firstRow):
                #Also, add to x & y_axis respectively
                x_axis.append(float(split_line[1]))
                y_axis.append(float(split_line[2]))
            firstRow = True

        #Add data to dictionary to sort
        #As of python 3.7, dictionaries are ordered!
        axisDict = {}
        for i in range(len(x_axis)):
            axisDict[x_axis[i]] = y_axis[i]

        #Now that it's sorted into a relationship, add data back
        #to axis lists
        sorted(axisDict)
        x_axis.clear()
        y_axis.clear()
        index = 0;
        for x_value in axisDict.keys():
            if (index != 0):
                x_axis.append(x_value)
                y_axis.append(axisDict[x_value])
            index += 1

        print("Post splitting....")
        print(x_axis)
        print(y_axis)

        #plot with matplotlib
        plt.scatter(x_axis, y_axis)

        #Generate trend line
        z = numpy.polyfit(x_axis, y_axis, 1) #Returns vector of coefficients
        p = numpy.poly1d(z) #Generates a polynomial from coefficients
        plt.plot(x_axis, p(x_axis), 'r-')

        plt.show()