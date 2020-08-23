# PyBank Assignmnet

# Import Modules/Libraries
import os
import csv 
import collections

# Creating the Path for the CSV file in Resources
file_path= os.path.join("Resources","election_data.csv")
# Defining all lists and variables
Total_Votes=0
votes_count=[]

with open(file_path,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

# Read each row of data after the header/Calculate the total number of votes cast
    for row in csvreader:
        Total_Votes +=1
        votes_count.append(row[2])

# Votes_Counter for Each Candidate/A complete list of candidates who received votes
    Votes_Counter= dict(collections.Counter(votes_count))
    print(Votes_Counter)

        
#Seperateing your keys from your values/The total number of votes each candidate won
    keys, values = zip(*Votes_Counter.items())
    Candidate_Names=keys
    Num_votes= values

# The percentage of votes each candidate won
    Khan_Ratio_Votes= (Num_votes[0]/Total_Votes)
    Khan_Percentage_Votes="{:.3%}".format(Khan_Ratio_Votes)

    Correy_Ratio_Votes= (Num_votes[1]/Total_Votes)
    Correy_Percentage_Votes="{:.3%}".format(Correy_Ratio_Votes)

    Li_Ratio_Votes= (Num_votes[2]/Total_Votes)
    Li_Percentage_Votes="{:.3%}".format(Li_Ratio_Votes)

    OTooly_Ratio_Votes= (Num_votes[3]/Total_Votes)
    OTooly_Percentage_Votes="{:.3%}".format(OTooly_Ratio_Votes)

# The winner of the election based on popular vote.
    Winner_Selector= max(Num_votes)
    Winner_Index= Num_votes.index(Winner_Selector)
    Winner_Name= Candidate_Names[Winner_Index]

# Printing all results
print("Election Results")
print("-"*40)
print(f"Total Votes: {Total_Votes})")
print("-"*40)
print(f"Khan: {Khan_Percentage_Votes} ({Num_votes[0]})")
print(f"Correy: {Correy_Percentage_Votes} ({Num_votes[1]})")
print(f"Li: {Li_Percentage_Votes} ({Num_votes[2]})")      
print(f"O\'Tooly: {OTooly_Percentage_Votes} ({Num_votes[3]})")
print("-"*40)
print(f"Winner: {Winner_Name}")


#Printing the results

    
# Export the caclulated results to a textfile

with open('PyPoll.txt','w') as text:
    text.write("Election Results\n")
    text.write("----------------------------------------\n")
    text.write(f"Total Votes: {Total_Votes}\n")
    text.write("----------------------------------------\n")
    text.write(f"Khan: {Khan_Percentage_Votes} ({Num_votes[0]})\n")
    text.write(f"Correy: {Correy_Percentage_Votes} ({Num_votes[1]})\n")
    text.write(f"Li: {Li_Percentage_Votes} ({Num_votes[2]})\n")      
    text.write(f"O\'Tooly: {OTooly_Percentage_Votes} ({Num_votes[3]})\n")
    text.write("----------------------------------------\n")
    text.write(f"Winner: {Winner_Name}\n")