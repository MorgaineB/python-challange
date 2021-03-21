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
    vote_counts = []

    #calculate the total number of votes cast
    for row in csv_reader:
        votes.append(row[0])
        total_votes = len(votes)
        #create list of unique candidates

        candidate = row[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1
        else:
            candidates.append(candidate)
            vote_counts.append(1)


#Print analysis to Terminal
print("Election Results")
print("------------------")
print("Total Votes ", total_votes)
print("------------------")

print(candidates)
print(vote_counts)

