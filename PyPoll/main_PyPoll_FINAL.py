# Import dependencies
import os, csv
from pathlib import Path 

# Assign file location with the pathlib library
# os.getcwd()
csv_file_path = Path('Resources','election_data.csv')

# Declare Variables 

# Open csv in default read mode with context manager
with open(csv_file_path,newline="", encoding="utf-8") as elections:
    csvreader = csv.reader(elections,delimiter=",")  # Store data under the csvreader variable
    header = next(csvreader)  # Skip the header so we iterate through the actual values
    
    total_votes = khan_votes = correy_votes = li_votes = otooley_votes = 0
    for row in csvreader: 
        total_votes +=1
        candidate_name = row[2]
        # We have four candidates if the name is found, count the times it appears
        if candidate_name == "Khan": 
            khan_votes +=1
        elif candidate_name == "Correy":
            correy_votes +=1
        elif candidate_name == "Li": 
            li_votes +=1
        elif candidate_name == "O'Tooley":
            otooley_votes +=1
# To find the winner we want to make a dictionary out of the two lists we previously created 
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]

# We zip them together the list of candidate(key) and the total votes(value)
# Return the winner using a max function of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# Print a the summary of the analysis
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print the summary table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Output files
# Assign output file location and with the pathlib library
# csv_file_path = Path('Resources','election_data.csv')
output_file = Path('Resources', 'Elections_Results_Summary.txt')

with open(output_file,"w") as file:
    file.write(f"Election Results")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Total Votes: {total_votes}")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    file.write("\n")
    file.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    file.write("\n")
    file.write(f"Li: {li_percent:.3f}% ({li_votes})")
    file.write("\n")
    file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    file.write("\n")
    file.write(f"----------------------------")
    file.write("\n")
    file.write(f"Winner: {key}")
    file.write("\n")
    file.write(f"----------------------------")
