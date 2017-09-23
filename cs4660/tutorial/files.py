"""Files tests simple file read related operations"""
from __future__ import division
class SimpleFile(object):
    """SimpleFile tests using file read api to do some simple math"""
    def __init__(self, file_path):
        self.numbers = []
        """
        TODO: reads the file by path and parse content into two
        dimension array (numbers)
        """
        f = open(file_path)
        for line in f:
            self.numbers.append(list(map(int,line.split(" "))))
        
    def get_mean(self, line_number):
        """
        get_mean retrieves the mean value of the list by line_number (starts
        with zero)
        """
        return sum(self.numbers[line_number])/len(self.numbers[line_number])

    def get_max(self, line_number):
        """
        get_max retrieves the maximum value of the list by line_number (starts
        with zero)
        """
        for number in self.numbers[line_number]:
            return(max(self.numbers[line_number]))

    def get_min(self, line_number):
        """
        get_min retrieves the minimum value of the list by line_number (starts
        with zero)
        """
        minnum = 0
        for number in self.numbers[line_number]:
            return(min(self.numbers[line_number]))

    def get_sum(self, line_number):
        """
        get_sum retrieves the sumation of the list by line_number (starts with
        zero)
        """
        sumofnum = 0
        for number in self.numbers[line_number]:
            sumofnum += number
        return sumofnum