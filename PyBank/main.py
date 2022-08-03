# In this challenge, you are tasked with creating a Python script to analyze the financial 
# records of your company. You will give a set of financial data called 
# [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: "Date" and "Profit/Losses". 
# (Thankfully, your company has rather lax standards for accounting, so the records are simple.)

# Your task is to create a Python script that analyzes the records to calculate each of the following:
 
# The total number of months included in the dataset

# * The net total amount of "Profit/Losses" over the entire period

# * The changes in "Profit/Losses" over the entire period, and then the average of those changes

# * The greatest increase in profits (date and amount) over the entire period

# * The greatest decrease in profits (date and amount) over the entire period

import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# total_months = []
# total_PL = {}
# profit = {}
# loses =[]
# profit_inc = []
# profit_dec = []


with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    # csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # # # Read each row of data after the header
    # for row in csvreader:
    #     print(row)

