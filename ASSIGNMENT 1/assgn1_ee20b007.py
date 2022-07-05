"""
        EE2703 Applied Programming Lab - 2022
        Assignment 1
        Name : Allu Yaswanth
        Roll Number : EE20B007
        Date : 26 Jan 2022
"""

#Importing sys
from sys import argv, exit


"""
Assigning constant variables to '.circuit' and '.end' for better readability
"""
SPICE_START = '.circuit'
SPICE_END = '.end'

global i 
i = 1

#Function to extract tokens from each line
def tokenExtract(line):
    global i
    line = line.split('#')[0]
    tokens = line.split()

      #For independent circuits(no. of tokens = 4)
    if len(tokens) == 4:
        elementType = tokens[0]
        fromNode = tokens[1]
        toNode = tokens[2]
        value = tokens[3]
        print("For the line : " , i)
        print(" Type : %s FromNode : %s  ToNode : %s Value : %s" % (elementType,fromNode,toNode,value))
        i += 1
        return [elementType,fromNode,toNode,value]
      #For voltage controlled voltage sources (no. of tokens = 6)
    elif len(tokens) == 6 :
        elementType = tokens[0]
        fromNode = tokens[1]
        toNode = tokens[2]
        volSource1 = tokens[3]
        volSource2 = tokens[4]
        value = tokens[5]
        print("For the line : " , i)
        print(" Type : %s FromNode : %s  ToNode : %s VolSource1 : %s VolSource : %s Value : %s" % (elementType,fromNode,toNode, volSource1, volSource2, value))
        i += 1
        return [elementType,fromNode,toNode,value]   
        
      #For current controlled voltage sources
    elif(len(tokens) == 5):
        elementType = tokens[0]
        fromNode = tokens[1]
        toNode = tokens[2]
        voltageSrc = tokens[3]
        value = tokens[4]
        print("For the line : " , i)
        print(" Type : %s FromNode : %s  ToNode : %s VoltageSource : %s Value : %s" % (elementType,fromNode,toNode, voltageSrc, value))
        i += 1
        return [elementType, fromNode, toNode, voltageSrc, value]
    else:
        print("For the line : " , i)
        print(' This is a invalid line')
        i += 1
        return []    
       

    



"""
Checking whether the number of arguments given are 2
if not through a error message and exit the program
"""
if len(argv) != 2:
    print('Please make sure that number of arguments must be 2')
    exit()

"""
Making sure to drop an error message if wrong file was given as an input using try-catch
"""
try:
    with open(argv[1]) as f:
        lines = f.readlines()
        f.close() # closing the file after reading
        start = -1; end = -2
        start_cnt = 0 
        end_cnt = 0

        for line in lines:              # extracting circuit definition start and end lines
            if  SPICE_START== line[:len(SPICE_START)]:
                start = lines.index(line)
                start_cnt +=1 #counting number of times '.circuit' was detected
            elif SPICE_END== line[:len(SPICE_END)]:
                end = lines.index(line)
                end_cnt +=1 #counting number of times '.end' was detected
                
        
        #validating circuit block,i.e. '.circuit' should always ahead of '.end'
        if start >= end:                
            print("Invalid circuit definition. It should start with '.circuit' and end with '.end'")
            exit(0)
        #if there are multiple '.circuit' or '.end', through an error message and exit the program
        if start_cnt != 1 or end_cnt != 1 :
            print("Your text should only contain one '.circuit' and one '.end', Your file may have multiple/no '.circuit' or '.end'")
            exit(0)
        
        for line in lines[start+1:end]:
           tokenExtract(line)      

         
        print("\nThe reversed output is :")
        #Reversing the lines
        for line in reversed([' '.join(reversed(line.split('#')[0].split()))
            for line in lines[start+1:end]]) :
                print(line)                 

except IOError:
    print('Invalid file. Make sure you entered correct file name')
    exit()


