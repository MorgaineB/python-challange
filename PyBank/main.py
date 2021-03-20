#import os to make code platform agnostic
import os 

#import csv to read csv file
import csv

#create a path to the csv file
csvpath = os.path.join("Resources", "budget_data.csv")

#read the csv file and construct csv reader, skip the header
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csv_reader)

    #define lists to store data
    months = []
    profit_loss = []
    changes = []
    greatest_increase_date = ''
    greatest_decrease_date = ''
    
    #Calculate the total number of months included in the dataset
    for row in csv_reader:
        months.append(row[0])
        total_months = len(months)

#Calculate the net total amount of "Profit/Losses" over the entire period
        profit_loss.append(int(row[1]))
        total_profit = sum(profit_loss)

    #Calculate the changes in "Profit/Losses" over the entire period
    for i in range (1, len(profit_loss)):
        changes.append(profit_loss[i] - profit_loss[i-1])

        #Find the average "Profit/Losses" change
        change_average = sum(changes)/len(changes)
       
  
#Find the average "Profit/Losses" change


#Calculate the greatest increase in profits (date and amount) over the entire period


#Calculate the greatest decrease in profits (date and amount) over the entire peiod


#Print analysis to Terminal
print("Financial Analysis")
print("---------------------------")
print("Total Months: ", total_months)
print("Net Total: ", total_profit)
print("Average Change: $", round(change_average, 2))

#Export analysis to a text file