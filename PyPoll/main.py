# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

# You will be given a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
# Your task is to create a Python script that analyzes the votes and calculates each of the followin
 
# The total number of votes cast

# * A complete list of candidates who received votes

# * The percentage of votes each candidate won

# * The total number of votes each candidate won

# * The winner of the election based on popular vote.

import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

total_votes = 0
Charles_Casper_Stockham = 0
Diana_DeGette = 0
Raymon_Anthony_Doane = 0

Candidates = []
Percentage = []
Can_Vote = []

with open (csvpath, encoding='utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")
    
    csv_header = next(csvreader)

    for row in csvreader:
    # The total number of votes cast
        total_votes = total_votes + 1
    # * A complete list of candidates who received votes
        if row[2] == "Charles Casper Stockham":
            Charles_Casper_Stockham = Charles_Casper_Stockham + 1
        elif row[2] == "Diana DeGette":
            Diana_DeGette = Diana_DeGette + 1
        elif row[2] == "Raymon Anthony Doane":
            Raymon_Anthony_Doane = Raymon_Anthony_Doane + 1

# Create list of candidates, voting results, and percentages
Candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
Can_Votes = [Charles_Casper_Stockham, Diana_DeGette, Raymon_Anthony_Doane]
Percentage = [(Charles_Casper_Stockham / total_votes) * 100, (Diana_DeGette / total_votes) * 100, (Raymon_Anthony_Doane / total_votes) * 100]

# zip lists together
Results = zip(Candidates, Percentage, Can_Votes)


for election_results in Results:
        print(f'Total Votes: {total_votes}')
        print(f'{election_results}')
        


        


# output_file = os.path.join("election_data.csv")
# # open the output file
# with open(output_file, "w") as datafile:
#     writer = csv.writer(datafile)

#     # Write the header row
#     writer.writerow(["Candidates", "Percentage", "CandidateVotes"])

#     # Write in zipped rows
#     writer.writerows(election_results)



        





    

    

