import re
from decimal import Decimal
import sys

def read_input_file(input_file, data_list):
    '''
    Summary:    Reads the input files and creates a data list of the input.
                Parses the 'Old' and 'New' values and appends it to the date.
    Input:      input_file - user input .txt file
                data_list - reference to create a list presented as '<value>;<date>'
    Output:     None
    '''
    try:
        f = open(input_file, 'r')
        line = f.readline()
        while line:
            #Date found in the current line
            date = re.match(r"^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d.\d\d\dZ", line).group(0)
            #Check if 'Old=' value is found in the current line of the streaming rate file
            if "Old" in line:
                old = re.search(r"Old=\d*.\d*", line).group(0).replace("Old=","")
                data_list.append("%s;%s"%(old,date))
            #Check if 'New=' value is found in the current line of the streaming rate file
            if "New" in line:
                new = re.search(r"New=\d*.\d*", line).group(0).replace("New=","")
                data_list.append("%s;%s"%(new,date))
            line = f.readline()
    finally:
        f.close()

def merge(left, right):
    '''
    Summary:    Merges two sub-lists (left abd right) into a results list
    Input:      left: halve array from [0:len/2]
                right: halve array from [len/2:len]
    Output:     The result of merging the two halves.
    '''
    result=[]
    x, y = 0, 0
    while(x<len(left) and y<len(right)):
        #compare the halves and append to list
        if(Decimal(left[x].split(';')[0])<=Decimal(right[y].split(';')[0])):
                result.append(left[x])
                x+=1
        else:
                result.append(right[y])
                y+=1

    #adding remainder to list
    result+=left[x:]
    #adding remainder to list
    result+=right[y:]
    
    return result


def merge_sort(input_list):
    '''
    Summary:    Using merge sort to sort the list collected for streaming data.
    Input:      input_list - the list to be sorted
    Output:     A sorted list
    '''
    #If there is only one item in the list, then return the list
    if(len(input_list)<2):
            return input_list
    #split the list into halves
    mid=len(input_list)/2

    #sort in halves
    left = merge_sort(input_list[:mid])
    right = merge_sort(input_list[mid:])
    
    return merge(left,right)

def main():
    '''
    Summary:    The main function to run when the user call this script.
    Input:      sys.argv[1] - a file of streaming rate
    Output:     Provides statistics
                    Average - Addition of the all the streaming rates.
                              It is divided by total provide.
                    Minimum - Minimum stream rate found in input file
                    Maximum - Maximum stream rate found in input file
                    Middle - Middle stream rate found in input file
    '''
    if len(sys.argv) != 2:
        print "Invalid arguments. Please enter one input file of streaming rate"
        sys.exit(-1)

    input_file = sys.argv[1]

    #ensure input is a text file
    if not(input_file.endswith('.txt')):
        print "Invalid user input type. It must be a .txt file"
        sys.exit(-1)

    #create a data_list from the file provide: '<value><date>'
    data_list = []
    read_input_file(input_file, data_list)
    data_list = merge_sort(data_list)

    #calculates the statistics
    size = len(data_list)
    average = 0
    for index in range(size):
        average+=Decimal(data_list[index].split(';')[0])
    average = round(average/size,3)
    minimum = data_list[0].split(';')
    maximum = data_list[-1].split(';')
    middle = data_list[size/2].split(';')
    print "Average is %s" % average
    print "Minimum is %s at time %s" % (minimum[0], minimum[1])
    print "Maximum is %s at time %s" % (maximum[0], maximum[1])
    print "Middle is %s at time %s" % (middle[0], middle[1])
    sys.exit(0)

main()
    

