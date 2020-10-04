#The data we need to retrieve
#1.The total number of vostes cast
#2.A complete list of candidated who received votes
#3.The percentage of votes each candidate won
#4.The total number of votes each candidate won
#5.The winner of the election based on popular vote
     
import csv
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to save the file to path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initiliaze a varible to zero, vote counter.
total_votes = 0
#New list to get candidates.
candidate_options = []
#Declare the empty dictionary
candidate_votes = {}
#Winning candidate and winning count tracker.
winning_candidate = " "
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:

    #To do: read and analyze the data.
    #Read the file object woth the reader function.
    file_reader = csv.reader(election_data)

    #Print the header row. Skip the first row and return the next item in the list.
    headers = next(file_reader)
    #Print each row in the CSV file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1
        #Print the candidate name from each row.
        candidate_name = row[2]
        #Add the candidate name to the candidate options list, get unique names
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            #Begin tracking that candidate's vote count. Set it to zero so we can start tallying the votes for each candidate.
            candidate_votes[candidate_name] = 0
        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

#Save teh results to our text file.
with open(file_to_save, "w") as txt_file:

    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)        

    #Detetermine the percentage of votes for each candidate by looping though the counts.
    #Iterate though the candidate list.
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        #Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #Save the candidate results to our text file.
        txt_file.write(candidate_results)

    #Determine winning vote count and candidate.
    #Determine if votes are greater than winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            #If true then set winning count + votes and winning_percent =
            #vote_percentage.
            winning_count = votes
            winning_candidate = candidate_name
            #Set the winning_candidate queal to the candidate's name
            winning_percentage = vote_percentage

        #Print the winning candidates' results to the terminal.
        winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    #Save the winning candidate;s result to the text file.    
    txt_file.write(winning_candidate_summary)






        


      

    

        

        

