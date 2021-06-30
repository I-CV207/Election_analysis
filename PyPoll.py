# Data to retrieve
# 1-Total number of votes cast
# 2-A complete list of candidates who received votes
# 3-Total number of votes each candidate received
# 4-Percentage of votes each candidate won
# 5-The winner of the election based on popular vote

# Add dependencies
import csv
import os
#Assign a variable for the file to load and the path
Election_results_file=os.path.join("Resources","election_results.csv")

# Assign variable to save file to a path
Save_results=os.path.join("analysis","election_analysis.txt")

#Open the election results and read the file
with open(Election_results_file) as election_data:

#To do: read and analyse the data here
    Election_read=csv.reader(election_data)
    # Read and print the header row.
    headers=next(Election_read)
    print(headers)

    