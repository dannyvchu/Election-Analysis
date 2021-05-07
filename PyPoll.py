# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_load = os.path.join('resources','election_results.csv')
# Assign a variable to save the file to a path.
file_save = os.path.join('analysis','election_analysis.txt')
# Setting total votes to 0
total_votes = 0
# Create candidates list
candidate_options = []
# Create dictionary to store votes.
candidate_votes ={}
# Winning Candidate and Winning Count Tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_load) as election_data:

    # Read the file object with the reader function.
    read = csv.reader(election_data)
    
    # Print the header row.
    headers = next(read)
    # print(headers)

    # Print each row in the CSV file.
    for row in read:
        
        # Add to the total vote count.
        total_votes += 1
                
        # Get the candidate names.
        candidate_name = row[2]
        
        # Adding unique candidate names.
        if candidate_name not in candidate_options:
            
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            
            # Begin tracking candidates vote.
            candidate_votes[candidate_name] = 0

         # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1   

# Save the results to our text file.
with open(file_save, 'w') as txt_file:

    # Print the final vote count to the terminal
    election_results = (
        f'\nElection Results\n'
        f'---------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'---------------------------\n')
    print(election_results, end='')
    # Save the final vote count to the txt file.
    txt_file.write(election_results)
            

    # Determine the percentage of votes for each 
    # candidate by looping through the count
    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        
        # Calculate the vote percentage
        (vote_percentage) = (votes/total_votes) * 100
    
        # Print the total votes and candidate names
        candidate_results = (f'{candidate_name}:{vote_percentage:.1f}% ({votes:,})\n')

        # Print each candidate, their voter count, and percentage to the terminal
        print(candidate_results)
        # Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine if the votes are greater than the winning count
        if (votes>winning_count) and (vote_percentage>winning_percentage):
            # If true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            
            # Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f'---------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'---------------------------\n')
    print(winning_candidate_summary)
    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

