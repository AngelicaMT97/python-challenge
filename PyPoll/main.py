import os
import csv

# Set the file paths
csv_path = "C:\\Users\\angel\\OneDrive\\Documentos\\Bootcamp\\Challenges\\Challenge 3\\python-challenge\\PyPoll\\Resources\\election_data.csv"
output_path = "C:\\Users\\angel\\OneDrive\\Documentos\\Bootcamp\\Challenges\\Challenge 3\\python-challenge\\PyPoll\\Analysis\\Analysis.txt"

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(csv_path, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)

    # Iterate through rows in the CSV
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

        # Update candidate votes
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            candidates[candidate_name] += 1

# Analyze the results
analysis_results = []

for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    analysis_results.append(f"{candidate}: {percentage:.3f}% ({votes})")

    # Check for the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

# Generate the analysis report
analysis_report = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
    + "\n".join(analysis_results)
    + "\n-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------"
)

# Print the analysis to the terminal
print(analysis_report)

# Export the analysis to a text file
with open(output_path, "w", newline="", encoding="utf-8") as txtfile:
    txtfile.write(analysis_report)

print("Analysis has been exported to", output_path)
