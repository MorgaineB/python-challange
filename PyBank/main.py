#import os to make code platform agnostic
import os 

#import csv to read csv file
import csv

#create a path to the csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#read the csv file and construct csv reader
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')


#Calculate the total number of months included in the dataset
    lines = len(list(csv_reader))
    print(lines)

#Calculate the net total amount of "Profit/Losses" over the entire period


#Calculate the changes in "Profit/Losses" over the entire period


#Find the average "Profit/Losses" change


#Calculate the greatest increase in profits (date and amount) over the entire period


#Calculate the greatest decrease in profits (date and amount) over the entire peiod


#Print analysis to Terminal


#Export analysis to a text file