# some common functions and varibles that will be 
# shared in different program
import csv
from classes import *
attris = ['Alt', 'Bar', 'Fri', 'Hun', 'Pat', 'Price', 'Rain', 'Res', 'Type', 'Est', 'classification']
def importData(file):
    """
    create examples from csv format file
    input: file name
    output: examples
    """
    with open(file,'rb') as csvfile:
	datareader = csv.reader(csvfile, delimiter = ',', quotechar='|')
        examples = []
	for row in datareader:
            pairs = []
            for i in range(len(row)):
                row[i] = row[i].replace(" ","")
                pairs.append((attris[i], row[i]))
            examples.append(Example(pairs))
    return examples
