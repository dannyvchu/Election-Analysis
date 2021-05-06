# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_load = os.path.join('resources','election_results.csv')
# Assign a variable to save the file to a path.
file_save = os.path.join('analysis','election_analysis.txt')

# Open the electionr esults and read the file.
with open(file_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    read = csv.reader(election_data)
    # Print the header row.
    headers = next(read)
    print(headers)