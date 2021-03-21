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

    percentages = []
    max_votes = vote_counts[0]
    max_index = 0
    #calculate the percentage of the vote each candidate got
    #find the winner
    for count in range(len(candidates)):
        vote_percentages = vote_counts[count]/total_votes*100
        percentages.append(vote_percentages)
        if vote_counts[count] > max_votes:
            max_votes = vote_counts[count]
            print(max_votes)
            max_index = count
    winner = candidates[max_index]


#Print analysis to Terminal
print("Election Results")
print("------------------")
print("Total Votes ", total_votes)
print("------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("------------------")
print("Winner: ", winner)

