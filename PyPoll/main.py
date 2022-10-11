import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

total_votes = 0
Charles_Casper_Stockham = 0
Diana_DeGette = 0
Raymon_Anthony_Doane = 0
Counter= 0
Winner = []
Candidates = []
Percentage = []
Can_Vote = []

with open (csvpath, encoding='utf') as csvfile:

    csvreader = csv.reader(csvfile, delimiter= ",")
    
    csv_header = next(csvreader)

    for row in csvreader:
    
        total_votes = total_votes + 1
    
        if row[2] == "Charles Casper Stockham":
            Charles_Casper_Stockham = Charles_Casper_Stockham + 1
        elif row[2] == "Diana DeGette":
            Diana_DeGette = Diana_DeGette + 1
        elif row[2] == "Raymon Anthony Doane":
            Raymon_Anthony_Doane = Raymon_Anthony_Doane + 1


        

Candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
Can_Votes = [Charles_Casper_Stockham, Diana_DeGette, Raymon_Anthony_Doane]
Percentage = [(Charles_Casper_Stockham / total_votes) * 100, (Diana_DeGette / total_votes) * 100, (Raymon_Anthony_Doane / total_votes) * 100]


Results = zip(Candidates, Percentage, Can_Votes)

print(f'Total Votes: {total_votes}')
for election_results in Results:
        print(f'{election_results}')
        print(f'Winner: {Winner}')
        



        





    

    

