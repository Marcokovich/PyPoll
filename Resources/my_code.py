# Add our dependencies.
import csv
import os

file_to_load = os.path.join("..", "Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initializing Variables, Lists and Dictionaries
#step 1 and step 2
total_votes = 0
candidate_options = []
candidate_votes = {}
winning_candidate = ""
winning_count = 0
winning_percentage = 0
winning_ccount = 0
winning_percentagec = 0
county_names = []
county_votes = {}
#open the election file with csv reader
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    #step 3
    for row in reader:

        #Adding each row to the vote count to the total vote count
        total_votes = total_votes + 1
        #getting each candidate/county name to initialize and fill in the respective list
        candidate_name = row[2]
        county_name = row[1]
        #code slightly modified to do the exact same thing.... but counties instead
        #step 4a
        if county_name not in county_names:
            county_names.append(county_name)
            #step 4c
            county_votes[county_name] = 0
        #step5
        county_votes[county_name] += 1
        #if not in statement to add candidate name to list and initialize the vote counter
        #step 4b
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        #adding the vote to the repsective candidate    
        candidate_votes[candidate_name] += 1
    #printing will be done at the end of the program
    #print(county_votes)
    #print(candidate_votes)

    #print(total_votes)
#initializing the county results.    
county_results = ("")    
#step 6a
for county_name in county_votes:
    #step 6b
    votec = county_votes.get(county_name)
    #step 6c
    vote_percentage_c = float(votec)/float(total_votes) * 100
    #getting the result from these calculations into a single string and then appending the county results with the string of each
    #individual outcome.
    county_result = (
    f"{county_name}: {vote_percentage_c:.1f}% ({votec:,})\n")
    county_results += county_result
    #I hope I still get points for 6d here, but as stated earlier for the sake of formatting, I will be saving the terminal printing
    #until the end
    #print(county_results)
    #calculating the winning values and highest voting county
    #step 6f
    if (votec > winning_ccount) and (vote_percentage_c > winning_percentagec):
        winning_ccount = votec
        winning_county = county_name
        winning_percentagec = vote_percentage_c

    winning_county_summary = (
    f"-------------------------\n"
    f"Largest County Turnout: {winning_county}\n"
    f"-------------------------\n")
#I hope I still get points for step 7 since I'm saving the printing until the end.    
#print(winning_county_summary)
#initialize results as string
candidate_results = ""
for candidate_name in candidate_votes:
    #step 6a, 6b, and 6c except that it is the candidates this time
    # Retrieve vote count and percentage
    votes = candidate_votes.get(candidate_name)
    vote_percentage = float(votes) / float(total_votes) * 100
    #append result string for clarity
    candidate_result = (
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    candidate_results += candidate_result
    #saving printing until the end to reduce confusionw
    #print(candidate_results)
    #calculate the winner and filling in the winner values.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
    #filling winner summary for file filling and printing at the end.
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    
#print(winning_candidate_summary)
#I'm a bit experienced with python, but mostly in data science. I want to try some more program oriented applications.
#As this is going to my github, I will flex a little to make my code a tad bit more appealing.
#I will be trying to use try and except to handle exceptions on my code. For this reason I will be uploading the resources without the
#results textfile
try:
    with open(file_to_save, "w") as txt_file:
        print("Text file Exists")
#using the exception to create the file
except FileNotFoundError:
    print("Text file Doesn't exist... yet")
    with open(file_to_save, "x") as txt_file:
        print("Text file now exists")
#file exists so code will be executed now.        
finally:
    with open(file_to_save, "w") as txt_file:
        #step 6e and step 8 are technically here
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            f"County Votes:\n"
            f"{county_results}\n"
            f"{winning_county_summary}"
            f"{candidate_results}"
            f"{winning_candidate_summary}")
        txt_file.write(election_results)
        #this is all of the printable steps in one line of code rather than running  print multiple times.
        print(election_results)


