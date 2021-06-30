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

#Initialize total vote counter.
total_votes=0

#Candidate options list
candidate_options=[]

#Empty dictionary for candidate votes
candidate_votes={}

#Winning candidate and winning count tracker
winning_candidate=""
winning_count=0
winning_percentage=0

#Open the election results and read the file
with open(Election_results_file) as election_data:

#To do: read and analyse the data here
    Election_read=csv.reader(election_data)
    # Read and print the header row.
    headers=next(Election_read)
    

    #Print each roe in the CSV file
    for row in Election_read:
        #Add to the total vote count.
        total_votes+=1
        #+= is similar as writing "total_votes=total_votes +1" to iterate

        #Print the candidate name for each row
        candidate_name=row[2]
        #if the candidate does not match any existing candidate...
        
        if candidate_name not in candidate_options:
            
            #Add the candidate name to the candidate options list
            candidate_options.append(candidate_name)
            
            # Begin tracking the candidate vote count
            candidate_votes[candidate_name]=0
            
        # Add a vote to the candidates count
        candidate_votes[candidate_name]+=1
      
    #iterate through the candidate list
for candidate_name in candidate_votes:
        
    #Retrieve vote count of a candidate
    votes=candidate_votes[candidate_name]
        
    #Calculate the percentage of votes
    vote_percentage=float(votes)/float(total_votes) * 100
    #Determine winning vote count and candidate
    #Determine if the votes is greater than the winning count
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        #If true set winning count = votes and winning_percent=vote percentage
        winning_count=votes
        winning_percentage=vote_percentage
        #And, set the winning candidate equal to the candidates name
        winning_candidate=candidate_name
    
    
    
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary=(
    f"-----------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,} votes\n"
    f"Winning Vote percentage: {winning_percentage:.1f}%\n"
    f"-----------------------------\n"
)
print(winning_candidate_summary)