# In this challenge, you are tasked with creating a Python script to analyze the financial 
# records of your company. You will give a set of financial data called 
# [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: "Date" and "Profit/Losses". 
# (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

total_months = []
total_PL = []
average_change = []
profit_inc = []
profit_dec = []

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    csv_header = next(csvreader)

    for row in csvreader:
        # The total number of months included in the dataset
        
        total_months.append(row[1])
        
        # * The net total amount of "Profit/Losses" over the entire period

        total_PL.append(int(row[2]))

        # * The changes in "Profit/Losses" over the entire period, and then the average of those changes
        
        # budgetdata = round(int(total_months / total_PL) * 100, 2)
        # average_change.append(str(budgetdata))
        
        # * The greatest increase in profits (date and amount) over the entire period

        profit_inc.append(max(int[row(2)]))

        # * The greatest decrease in profits (date and amount) over the entire period
        
        profit_dec.append(min(int[row(2)]))


print(str(len(total_months)))
print(str(len(total_PL)))
# print(str(int(average_change)))
print(str(int(profit_inc)))
print(str(int(profit_dec)))



















