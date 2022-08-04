# In this challenge, you are tasked with creating a Python script to analyze the financial 
# records of your company. You will give a set of financial data called 
# [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: "Date" and "Profit/Losses". 
# (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

total_months = 0
total_PL = 0
average_change = 0
profit_inc = 0
profit_dec = 0

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    csv_header = next(csvreader)

    for row in csvreader:
        # The total number of months included in the dataset
        
        total_months +=1
        
        # * The net total amount of "Profit/Losses" over the entire period

        total_PL.append(int(row[1]))

        # * The changes in "Profit/Losses" over the entire period, and then the average of those changes
        
        budgetdata = round(int(total_months / total_PL) * 100, 2)
        average_change.append(str(budgetdata + 1))
        
        # * The greatest increase in profits (date and amount) over the entire period

        profit_inc.append(max(int[row(1)]))

        # * The greatest decrease in profits (date and amount) over the entire period
        
        profit_dec.append(min(int[row(1)]))


print(total_months)
print(str(total_PL))
print(str(int(average_change)))
print(str(int(profit_inc)))
print(str(int(profit_dec)))



















