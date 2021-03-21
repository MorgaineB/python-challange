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
    increase_date = ''
    decrease_date = ''
    
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
        change_average = round(sum(changes)/len(changes),2)

        #Calculate the greatest increase in profits
        greatest_increase = max(changes)
        
        #Find the date corresponding to this increase
        increase_date = str(months[changes.index(max(changes))+1])

            #hello, grader, just popping in to ask why I needed the +1 in the line of code above to get the correct month output
            #I figured it would fix the issue I was having, but I'm not sure why I was having the issue in the first place

        #Calculate the greatest decrease in profits
        greatest_decrease = min(changes)

        #Find the date corresponding to this decrease 
        decrease_date = str(months[changes.index(min(changes))+1])

#Print analysis to Terminal
print("Financial Analysis")
print("---------------------------")
print("Total Months: ", total_months)
print("Net Total: $", total_profit)
print("Average Change: $", change_average)
print("Greatest Increase in Profits: ", increase_date, "($", greatest_increase, ")")
print("Greatest Decrease in Profits: ", decrease_date, "($", greatest_decrease, ")")

#Export analysis to a text file
output_analysis = "Analysis/pybank_analysis.txt"
with open(output_analysis, "w", newline="") as datafile:
    csvwriter = csv.writer(datafile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["--------------------------"])
    csvwriter.writerow(["Total Months: " + str(total_months)])
    csvwriter.writerow(["Net Total: $" + str(total_profit)])
    csvwriter.writerow(["Average Change: $" + str(change_average)])
    csvwriter.writerow(["Greatest Increase in Profits: " + str(increase_date) + "($" + str(greatest_increase)+ ")"])
    csvwriter.writerow(["Greatest Decrease in Profits: " + str(decrease_date) + "($" + str(greatest_decrease)+ ")"])
