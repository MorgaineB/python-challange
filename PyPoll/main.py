#import os to make code platform agnostic
import os

#import csv to read csv file
import csv

#create a path to the csv file
csvpath = os.path.join("Resources", "election_data.csv")

#read the csv file and construct csv reader, skip the header
with open(csvpath, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csv_reader)

    #define lists to store data
    votes = []
    candidates = []

    #calculate the total number of votes cast
    for row in csv_reader:
        votes.append(row[0])
        total_votes = len(votes)
        #create list of unique candidates
        if row [2] not in candidates:
            candidates.append(row[2])

#Print analysis to Terminal
print("Election Results")
print("------------------")
print("Total Votes ", total_votes)
print("------------------")



