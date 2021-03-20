#import os to make code platform agnostic
import os 

#import csv to read csv file
import csv

#create a path to the csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#read the csv file and construct csv reader
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')


