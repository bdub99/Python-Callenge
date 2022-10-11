import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
# set variables
months =[]
profit_loss = []

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter= ",")
    
    csv_header = next(csvreader)

    for row in csvreader:
        
        months.append(row[0])
        
        profit_loss.append(float(row[1]))

total_months = (len(months))

net = sum(profit_loss)

average_change = net/total_months

max_profit = max(profit_loss)

index_max = profit_loss.index(max_profit)
max_month = months[index_max]

min_profit = min(profit_loss)

index_min = profit_loss.index(min_profit)
min_month = months[index_min]

print(f"Total Month: {total_months}")
print(f"Total: {net}")
print(f"Average Change; {average_change}")
print(f"Greatest Increase ; {max_month} {max_profit}")
print(f"Greatest Decrease : {min_month} {min_profit}")



















