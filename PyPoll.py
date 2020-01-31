# add our dependencies
import csv
import os

# assign a variable to load a file form a path
file_to_load = os.path.join("Resources/election_results.csv")
# assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the elction results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # read and print the header row.
    headers = next(file_reader)
    print(headers)

