# install modules
import csv
import os

#declare variables
total_votes = 0
VoterID = []
county = []
candidate = ""
unique_candidate = {}
candidate_votes = []
total_candidate_vote = 0
winner = ""
winner_vote = 0


# Set path for file
csvpath = os.path.join("..", "Data", "election_data.csv")

with open(csvpath, newline='') as election_csv_file:

    election_csvreader = csv.reader(election_csv_file, delimiter=',')
    election_header = next(election_csvreader)

    for row in election_csvreader:
    
        VoterID.append(row[0])
        county.append(row[1])
        candidate = (row[2])

        # total number of months
        total_votes = total_votes + 1


        if candidate in unique_candidate.keys():
            unique_candidate[candidate].append(1)

        else:
            unique_candidate[candidate] = [1]

    print("Election Results")
    print("-----------------------------------")
    print(f"Total Votes: {str(total_votes)}")
    print("-----------------------------------")

    for key in unique_candidate:
        value = unique_candidate[key]
        total_candidate_vote = (sum(value))
        vote_percentage = ((total_candidate_vote / total_votes) * 100)

        if winner_vote < total_candidate_vote:
            winner = key
            winner_vote = total_candidate_vote


        print(key + ": " + '{:,.3f}'.format(vote_percentage) + "%" + " (" + str(total_candidate_vote) + ")")
    print("-----------------------------------")
    print("Winner: " + winner)

#exporting result to txt file
PyPoll_export = open("PyPoll.txt", "w")

PyPoll_export.write("Election Results\n")
PyPoll_export.write("-----------------------------------\n")
PyPoll_export.write(f"Total Votes: {str(total_votes)}\n")
PyPoll_export.write("-----------------------------------\n")

for key in unique_candidate:
        value = unique_candidate[key]
        total_candidate_vote = (sum(value))
        vote_percentage = ((total_candidate_vote / total_votes) * 100)

        if winner_vote < total_candidate_vote:
            winner = key
            winner_vote = total_candidate_vote


        PyPoll_export.write(key + ": " + '{:,.3f}'.format(vote_percentage) + "%" + " (" + str(total_candidate_vote) + ")\n")
PyPoll_export.write("-----------------------------------\n")
PyPoll_export.write("Winner: " + winner)

PyPoll_export.close()