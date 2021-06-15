#Michael Patrick
#6/13/21
#Matplot from CSV example
#Takes a CSV value, formatted as specified below,
#and generates a plot using MatPlotLib.

import csv
import matplotlib.pyplot as plt
import numpy

#The AxisGenerator class reads in data from a CSV
#file and returns a list of lists describing the
#y_axis and multiple x_axes. Expects the structure
#to be as follows:
#
#Name   Measurement1 Measurement2 ... Measurement N
#[name]      [float]      [float]           [float]
#.
#.
#.
#
#Note: the first column will be considered the y-axis
#AxisGenerator requires two paramaters for initialization:
#"file_name" : the file name of the CSV file (should be in same directory)
#"num_axes" : the number of axes expected to be read, or number of columns
#NOT including the first.
class CSVtoPlot:

    #Initializes the list of identifiers for each access by putting each
    #in a list in the expected fashion:
    #["Name", "Y_Axis Name", "X_Axis 1 Name", "X_Axis 2 Name", ... "X_Axis N Name"
    #
    #"list_of_names" : a list of names separated by commas, i.e, "Name, Length, Height"
    def init_names(self, list_of_names):
        split_string = list_of_names.split(',')
        for string in split_string:
            if (string[0] == '\ufeff'):
                self.axes_names.append(string[1:len(string)])
            else:
                self.axes_names.append(string[0:len(string)])

    #Generate a dictionary of float value mapped to a list of floats.
    #Edits the object's axis_map data member
    #"file_name" is the name of a csv file (in same directory)
    #"num_axes" is the number of total columns - 2
    def create_dict(self, file_name, num_axes):
        #Then reads in from the file and does preliminary load
        with (open(file_name, encoding="utf-8", newline='')) as csvfile:
            csvreader = csv.reader(csvfile, delimiter = ' ')

            is_first = True;
            #y_value key to list of all x_values
            for row in csvreader:
                split_string = row[0].split(',')

                if(is_first): #skip name
                    is_first = False
                    continue

                #Add each x_axis value to list x_values mapped to
                #the y_axis value

                #Check if key already exists. If it does, do nothing.
                #Oterhwise, map empty list to that key
                if (float(split_string[1]) not in self.axis_map.keys()):
                    self.axis_map[float(split_string[1])] = []
                for x in range(2, num_axes + 2): #Not inclusive!
                    self.axis_map[float(split_string[1])].append(float(split_string[x]))


    #Ensures that all lists of x values are sorted in self.axes_map
    def sort_x_values(self):
        for key in self.axis_map.keys():
            if(len(self.axis_map[key]) > 1): #OK to skip if only 1
                self.axis_map[key].sort()

    #Initializes axes data members with the correct ORDERED values
    def init_axes(self):
        for key in sorted(self.axis_map.keys()): #should be added in sorted value
            for x in range(len(self.axis_map[key])):
                self.y_axis.append(key)

        self.x_axes.append([])
        for key in sorted(self.axis_map.keys()):
            for x in range(len(self.axis_map[key])):
                self.x_axes[0].append(self.axis_map[key][x]) #hard coded 0


        print(self.axis_map)
        print("X:", self.x_axes)
        print("Y:", self.y_axis)

        assert len(self.x_axes[0]) == len(self.y_axis)

    #Initialized with a filename ("somename.csv") and the total number
    #of columns - 2
    def __init__(self, file_name, num_axes):
        assert num_axes > 0, "num_axes must be > 0"

        self.x_axes = [] #intended to be list of lists of floats
        self.y_axis = [] #list of floats
        self.axis_map = {}
        self.axes_names = [] #TODO: fill in

        self.create_dict(file_name, num_axes) #Map y values to x values
        self.sort_x_values() #sort x values

        self.init_axes() #Add to appropriate data members

    #Uses initialized x and y axes to construct a scatter plot using matplotlib
    def make_scatter(self):
        #plot
        plt.scatter(self.x_axes[0], self.y_axis)

        #trend line
        z = numpy.polyfit(self.x_axes[0], self.y_axis, 1) #Returns vector of coefficients
        p = numpy.poly1d(z) #Generates a polynomial from coefficients
        plt.plot(self.x_axes[0], p(self.x_axes[0]), 'r-')

        #Output
        plt.show()

    #Makes a line graph 
    def make_line(self):
        fig, ax = plt.subplots()
        ax.plot(self.y_axis, self.x_axes[0])
        plt.show()

if __name__ == '__main__':
    converter = CSVtoPlot('ExampleCSV.csv', 1)
    converter.make_line()


    """
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
    """