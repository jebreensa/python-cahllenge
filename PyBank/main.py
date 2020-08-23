# PyBank Assignmnet

# Import Modules/Libraries
import os
import csv 
import statistics

# Creating the Path for the CSV file in Resources
file_path= os.path.join("Resources","budget_data.csv")

# Defining all lists and variables
Total_Months=0
Pi=0
Total_Profit=0
date=[]
Profit_Losses=[]
Monthly_Change=[]

with open(file_path,"r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

# Read each row of data after the header
    for row in csvreader:
        Total_Months +=1
        Total_Profit += int(row[1])
        date.append(row[0])
        Pf= int(row[1])
        Monthly_Profit_Change= Pf-Pi
        Monthly_Change.append(Monthly_Profit_Change)
        Pi=Pf
       
        

# The Total Number of Months included in the dataset
# Total_Months
# The net total amount of "Profit/Losses" over the entire period
# Total_Profit
# The average of the changes in "Profit/Losses" over the entire period
Average_changes= statistics.mean(Monthly_Change)

# The greatest increase in profits (date and amount) over the entire period
Greatest_Increase= max(Monthly_Change)
Greatest_Increase_Date= date[Monthly_Change.index(Greatest_Increase)]

# The greatest decrease in losses (date and amount) over the entire period
Greatest_Decrease= min(Monthly_Change)
Greatest_Decrease_Date = date[Monthly_Change.index(Greatest_Decrease)]

#Printing the Results

print("Financial Analysis")
print("-"*40)
print(f"Total Months: {Total_Months}")
print(f"Total: ${Total_Profit}")
print(f"Average Change: ${Average_changes}")
print(f"Greatest Increase in profits: {Greatest_Increase_Date} $({Greatest_Increase})")
print(f"Greatest Increase in profits: {Greatest_Decrease_Date} $({Greatest_Decrease})")

#Export the caclulated results to a textfile

with open('PyBank.txt','w') as text:

 text.write("Financial Analysis\n")
 text.write("----------------------------------------\n")
 text.write(f"Total Months: {Total_Months}\n")
 text.write(f"Total: ${Total_Profit}\n")
 text.write(f"Average Change: ${Average_changes}\n")
 text.write(f"Greatest Increase in profits: {Greatest_Increase_Date} $({Greatest_Increase})\n")
 text.write(f"Greatest Increase in profits: {Greatest_Decrease_Date} $({Greatest_Decrease})\n")
