import os
import csv

election_csv = os.path.join("Resources", "election_data.csv")

line_count = 0
candidates = []
candidate_votes ={}
winner_name = ""
winner_count = 0 

with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
 # Skip the header 
    next(csvreader, None)

    for row in csvreader: 
        # Count the total number of votes
        line_count += 1
        # Create a list of candidates' names
        name = row[2]
        if name not in candidates:
            candidates.append(name)
            candidate_votes[name] = 0 
        candidate_votes[name] += 1 
output = os.path.join("Analysis", "election_analysis.txt")         
with open(output, 'w') as file:
    election_output = ('Election Results\n'
    '-------------------------\n'
    f'Total votes: {line_count}\n'
    '-------------------------\n')
    print(election_output)
    file.write(election_output)

    for name in candidate_votes:
        vote = candidate_votes.get(name)
        percent = vote/line_count*100
        if vote > winner_count:
            winner_count = vote
            winner_name = name 


        vote_output = f'{name}: {percent:.3f}% ({vote})\n'
        print(vote_output)
        file.write(vote_output)
    winner = (f"""
-------------------------
Winner: {winner_name}
-------------------------
    """)   
    print(winner)
    file.write(winner)

