#Michael Patrick
#6/13/21
#Matplot from CSV example
#Takes a CSV value, formatted as specified below,
#and generates a plot using MatPlotLib.

import csv
import matplotlib.pyplot as plt
import numpy

#The CSVtoPlot class reads in data from a CSV
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
#"file_name" : the file name of the CSV file (should be in same directory). This file is expected to have a single
#x and y-axis
class CSVtoPlot:

    #Initializes the list of identifiers for each access by putting each
    #in a list in the expected fashion:
    #["Name", "X_Axis Name", "Y_Axis 1 Name", "Y_Axis 2 Name", ... "Y_Axis N Name"
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
    def create_dict(self, file_name):
        #Then reads in from the file and does preliminary load
        with (open(file_name, encoding="utf-8", newline='')) as csvfile:
            csvreader = csv.reader(csvfile, delimiter = ' ')

            is_first = True;
            #y_value key to list of all x_values
            for row in csvreader:
                split_string = row[0].split(',')

                if(is_first): #skip name
                    self.init_names(row[0])
                    is_first = False
                    continue

                #Add each y_axis value to list y_values mapped to
                #the x_axis value

                #Check if key already exists. If it does, do nothing.
                #Oterhwise, map empty list to that key
                if (float(split_string[1]) not in self.axis_map.keys()):
                    self.axis_map[float(split_string[1])] = []

                self.axis_map[float(split_string[1])].append(float(split_string[2]))


    #Ensures that all lists of x values are sorted in self.axes_map
    def sort_y_values(self):
        for key in self.axis_map.keys():
            if(len(self.axis_map[key]) > 1): #OK to skip if only 1
                self.axis_map[key].sort()

    #Initializes axes data members with the correct ORDERED values
    def init_axes(self):
        for key in sorted(self.axis_map.keys()): #should be added in sorted value
            for i in range(len(self.axis_map[key])):
                self.x_axis.append(key)

        for key in sorted(self.axis_map.keys()):
            for i in range(len(self.axis_map[key])):
                self.y_axis.append(self.axis_map[key][i]) #hard coded 0


        print(self.axis_map)
        print("X:", self.x_axis)
        print("Y:", self.y_axis)

        assert len(self.x_axis) == len(self.y_axis)

    #Initialized with a filename ("somename.csv") that has a single x-axis and single y-axis
    #Precondition: File must be formatted as specified above
    #Postcondition: Inititalizes a CSVtoPlot object
    def __init__(self, file_name):

        self.x_axis = [] #list of floats
        self.y_axis = [] #list of floats
        self.axis_map = {}
        self.axes_names = []

        self.create_dict(file_name) #Map y values to x values
        self.sort_y_values() #sort y values

        self.init_axes() #Add to appropriate data members

    #Uses initialized x and y axes to construct a scatter plot using matplotlib
    # Postcondition: outputs a matplotlib graph
    def make_scatter(self):
        #plot
        plt.scatter(self.x_axis, self.y_axis)

        #axes labels
        plt.xlabel(self.axes_names[1])
        plt.ylabel(self.axes_names[2])

        #trend line
        z = numpy.polyfit(self.x_axis, self.y_axis, 1) #Returns vector of coefficients
        p = numpy.poly1d(z) #Generates a polynomial from coefficients
        plt.plot(self.x_axis, p(self.x_axis), 'r-')

        #Output
        plt.show()

    #Makes a line graph
    #Postcondition: outputs a matplotlib graph
    def make_line(self):
        fig, ax = plt.subplots()
        ax.plot(self.x_axis, self.y_axis)
        ax.set_xlabel(self.axes_names[1])
        ax.set_ylabel(self.axes_names[2])
        plt.show()

if __name__ == '__main__':
    converter = CSVtoPlot('ExampleCSV.csv')
    converter.make_line()
