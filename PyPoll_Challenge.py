# add our dependencies
import csv
import os

# print and save to txt_file
def output_text(txt_file, message):
    print(message, end="")
    txt_file.write(message)

def election_analysis(input_file = "election_results.csv", output_file = "election_analysis.txt"):

    # ===================================
    # read and parse the election data
    # ===================================
    # initialize the total vote counter.
    total_votes = 0

    # candidates and candidate votes in dictionary
    candidates = []
    candidate_votes = {}

    # voter counties and county votes in dictionary
    counties = []
    county_votes = {}

    # open the election results and read the file.
    with open(input_file) as election_data:
        # csv reader.
        file_reader = csv.reader(election_data)

        # skip the header row.
        next(file_reader)

        # parse each line (row) in the csv file.
        for line in file_reader:
            total_votes += 1

            # count per candidate 
            candidate = line[2]
            if candidate not in candidates:
                candidates.append(candidate)
                candidate_votes[candidate] = 0
            candidate_votes[candidate] += 1
        
            # count per voter county
            voter_county = line[1]
            if voter_county not in counties:
                counties.append(voter_county)
                county_votes[voter_county] = 0
            county_votes[voter_county] += 1
    
    # ===================================
    # analysis and output the election results
    # ===================================
    with open(output_file, "w") as txt_file:
        # print the final vote result
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        # print and save the final vote count to the text file.
        output_text(txt_file, election_results)

        # county vote result
        # header
        output_text(txt_file, "\nCounty Votes:\n")
        
        most_votes = 0
        most_vote_county = ""
        for county in county_votes:
            votes = county_votes[county]
            percentage = float(votes) / float(total_votes) * 100
            election_results = (
                f"{county}: {percentage:.1f}% ({votes:,})\n"
            )
            output_text(txt_file, election_results)
            # largest turnout county
            if most_votes < county_votes[county]:
                most_votes = county_votes[county]
                most_vote_county = county
        # print and save largest turnout county
        election_results = (
            f"\n-------------------------\n"
            f"Largest County Turnout: {most_vote_county}\n"
            f"-------------------------\n")
        output_text(txt_file, election_results)

        # determine the winning candidate
        output_text(txt_file, "\nCandidate Votes:\n")

        winner = ""
        winning_count = 0
        winning_percentage = 0
        for candidate in candidate_votes:
            votes = candidate_votes[candidate]
            percentage = float(votes) / float(total_votes) * 100
            election_results = (
                f"{candidate}: {percentage:.1f}% ({votes:,})\n"
            )
            output_text(txt_file, election_results)

            # figure out the winner
            if votes > winning_count:
                winner = candidate
                winning_count = votes
                winning_percentage = percentage

        # print and save the winning results.
        election_results = (
            f"-------------------------\n"
            f"Winner: {winner}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        # print and save the winning candidate's results to the text file.
        output_text(txt_file, election_results)

        # all done
        output_text(txt_file, "\n")


# give csv election data in file_to_load, 
# output analysis result in file_to_save
# should work for california too  
if __name__ == "__main__":
    # assign a variable to load a file form a path
    file_to_load = os.path.join("Resources/election_results.csv")
    # assign a variable to save the file to a path
    file_to_save = os.path.join("analysis", "election_analysis.txt")

    # output analysis result in file_to_save 
    election_analysis(file_to_load, file_to_save)
