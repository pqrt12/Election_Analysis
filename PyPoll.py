# add our dependencies
import csv
import os

# assign a variable to load a file form a path
file_to_load = os.path.join("Resources/election_results.csv")
# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize a total vote counter.
total_votes = 0

# candidate options
candidates = []

# candidate votes in dictionary
candidate_votes = {}

# open the elction results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # read and print the header row.
    headers = next(file_reader)

    # parse each line in the csv file.
    for row in file_reader:
        total_votes += 1

        candidate = row[2]
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        
        candidate_votes[candidate] += 1
        
# determine the winner
winner = ""
winning_count = 0
winning_percentage = 0
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    if votes > winning_count:
        winner = candidate
        winning_count = votes

winning_result_summary = (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_result_summary)

with open(file_to_save, "w") as txt_file:
    # print the final vote result
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)    

    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {percentage:.1f}% ({votes:,})\n"
        )
        print(candidate_results)
        txt_file.write(candidate_results)

        # figure out the winner
        if votes > winning_count:
            winner = candidate
            winning_count = votes
            winning_percentage = percentage

    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
