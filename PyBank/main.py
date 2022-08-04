# In this challenge, you are tasked with creating a Python script to analyze the financial 
# records of your company. You will give a set of financial data called 
# [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: "Date" and "Profit/Losses". 
# (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
# set variables
total_months = 0
total_PL = 0
average_change = 0
profit_inc = []
profit_dec = []
profit = 0
loses = 0 


with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    csv_header = next(csvreader)

    for row in csvreader:
        # The total number of months included in the dataset
        
        total_months = total_months + 1
        
        # * The net total amount of "Profit/Losses" over the entire period
        if (int(row[1]) > 0):
            profit
        else: 
            (int(row[1]) < 0)
            loses 
        total_PL = profit - loses

        # * The changes in "Profit/Losses" over the entire period, and then the average of those changes
        def average(changes):
            length = len(changes) 
            average_change = 0.0
            for change in changes:
                average_change += changes
            return average_change / length

        # * The greatest increase in profits (date and amount) over the entire period

        profit_inc = [max(row(1))]

        # * The greatest decrease in profits (date and amount) over the entire period
        
        profit_dec = [min(row(1))]


print(total_months)
print(str(total_PL))
print(str(average))
print(f"{str(profit_inc)}")
print(f"{str(profit_dec)}")



















